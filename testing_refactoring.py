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
            result = subprocess.run(
                ["python3", temp_file.name],
                capture_output=True,
                text=True,
                timeout=10
            )
            output = result.stdout + result.stderr
            success = "AssertionError" not in output and result.returncode == 0
        except subprocess.TimeoutExpired:
            success = False
            output = "Timeout occurred"
    return success, output

def test_humaneval_with_tool(dataset_path):
    results = []
    with open(dataset_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= 50:  
                break
            
            problem = json.loads(line)
            task_id = problem['task_id']
            original_code = problem['canonical_solution']
            test_cases = problem['test']

            refactored_code, explanation = refactor_code_with_tool(original_code)

            original_success, original_output = run_tests(original_code, test_cases)

            if refactored_code:
                refactored_success, refactored_output = run_tests(refactored_code, test_cases)
            else:
                refactored_success, refactored_output = False, "Refactoring failed."

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
    original_passed = sum(1 for result in results if result['original_success'])
    refactored_passed = sum(1 for result in results if result['refactored_success'])
    improved = sum(
        1 for result in results
        if result['refactored_success'] and not result['original_success']
    )
    regressed = sum(
        1 for result in results
        if not result['refactored_success'] and result['original_success']
    )

    metrics = {
        "Total Tasks": total_tasks,
        "Original Success Rate": (original_passed / total_tasks) * 100,
        "Refactored Success Rate": (refactored_passed / total_tasks) * 100,
        "Improvement Rate": (improved / total_tasks) * 100,
        "Regression Rate": (regressed / total_tasks) * 100,
    }

    return metrics



metrics = calculate_results(results)

for key, value in metrics.items():
    print(f"{key}: {value:.2f}%")