import json
import tempfile
import subprocess
from processing import initialize_vectorstore, generate_code_assistance_prompt, get_ai_assistance, get_relevant_context

vector_store = initialize_vectorstore()

def refactor_code_with_tool(code, language="Python"):
    task = "Refactor Code"
    context = get_relevant_context(vector_store, code)
    prompt = generate_code_assistance_prompt(code, task, language, context)
    ai_response = get_ai_assistance(prompt, task)

    try:
        response_json = json.loads(ai_response) 
        if "code" in response_json:
            return response_json["code"], response_json.get("explanation", "")
        else:
            return None, "Response JSON missing 'code' field."
    except json.JSONDecodeError:
        return None, f"Failed to parse JSON. Raw response: {ai_response}"

def run_tests(code, test_cases):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as temp_file:
        temp_file.write(code + "\n" + test_cases)
        temp_file.flush()
        try:
            result = subprocess.run(["python3", temp_file.name], capture_output=True, text=True, timeout=10)
            success = result.returncode == 0
            output = result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            success = False
            output = "Timeout occurred"
    return success, output

def test_humaneval_with_tool(dataset_path):
    results = []
    with open(dataset_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= 10:  
                break
            
            print("=============================================================")
            problem = json.loads(line)
            task_id = problem['task_id']
            prompt = problem['prompt']
            entry_point = problem['entry_point']
            canonical_solution = problem['canonical_solution']
            test_cases = problem['test']

            original_code = f"{prompt}\n{canonical_solution}"

            print("-------------------------------")
            print(f"Task {task_id}:")
            print(f"Original Code:")
            print(original_code)
            print(f"Test Cases:")
            print(test_cases)
            print("-------------------------------")
            
            original_success, original_output = run_tests(original_code, test_cases)
            print("-------------------------------")
            print(f"original_success:")
            print(original_success)
            print(f"original_output:")
            print(original_output)
            print("-------------------------------")

            refactored_code, explanation = refactor_code_with_tool(original_code)
            print("-------------------------------")
            print(f"Refactored Code:")
            print(refactored_code)
            print(f"Explanation:")
            print(explanation)
            print("-------------------------------")

            if refactored_code:
                refactored_success, refactored_output = run_tests(refactored_code, test_cases)
            else:
                refactored_success, refactored_output = False, "Refactoring failed."

            print("-------------------------------")    
            print(f"refactored_success:")
            print(refactored_success)
            print(f"refactored_output:")
            print(refactored_output)
            print("-------------------------------")

            results.append({
                "task_id": task_id,
                "original_success": original_success,
                "refactored_success": refactored_success,
                "explanation": explanation,
                "original_output": original_output,
                "refactored_output": refactored_output,
            })

    return results

dataset_path = 'human-eval-v2-20210705.jsonl'
results = test_humaneval_with_tool(dataset_path)


def calculate_results(results):
    """
    Calculate metrics for original and refactored code.
    """
    total_tasks = len(results)
    #original_passed = sum(1 for result in results if result['original_success'])
    refactored_passed = sum(1 for result in results if result['refactored_success'])
    '''
    improved = sum(
        1 for result in results
        if result['refactored_success'] and not result['original_success']
    )
    regressed = sum(
        1 for result in results
        if not result['refactored_success'] and result['original_success']
    )
    '''
    total_tasks = len(results)
    total_code_correctness = 0
    total_passed = 0

    for result in results:
        if result["refactored_success"]:  
            total_code_correctness += 1  # CCS=1 for passing test cases
            total_passed += 1
        else:  
            total_code_correctness += 0  # CCS=0 for failing test cases
    average_code_correctness = total_code_correctness / total_tasks

    metrics = {
        "Total Tasks": total_tasks,
        #"Original Success Rate": (original_passed / total_tasks) * 100,
        "Refactored Success Rate": (refactored_passed / total_tasks) * 100,
        "Average Code Correctness": average_code_correctness * 100,  # Convert to percentage
        "Code Correctness (Passed Tasks)": total_passed,
        #"Improvement Rate": (improved / total_tasks) * 100,
        #"Regression Rate": (regressed / total_tasks) * 100,
    }

    return metrics



metrics = calculate_results(results)

for key, value in metrics.items():
    print(f"{key}: {value:.2f}%")