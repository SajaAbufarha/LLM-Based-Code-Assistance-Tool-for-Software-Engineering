import json
import tempfile
import subprocess
from processing import initialize_vectorstore, generate_code_assistance_prompt, get_ai_assistance, get_relevant_context

vector_store = initialize_vectorstore()

def generate_tests_with_tool(code, language="Python"):
    task = "Generate Tests"
    context = get_relevant_context(vector_store, code)
    prompt = generate_code_assistance_prompt(code, task, language, context)
    ai_response = get_ai_assistance(prompt, task)

    try:
        response_json = json.loads(ai_response) 
        if "tests" in response_json:
            return response_json["tests"], response_json.get("explanation", "")
        else:
            return None, "Response JSON missing 'tests' field."
    except json.JSONDecodeError:
        return None, f"Failed to parse JSON. Raw response: {ai_response}"

def run_generated_tests(canonical_solution, generated_tests):
    if not generated_tests:
        return False, "No tests generated"

    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_file:
        temp_file.write(canonical_solution + "\n" + generated_tests)
        temp_file.flush()
        try:
            result = subprocess.run(["python3", temp_file.name], capture_output=True, text=True, timeout=10)
            success = result.returncode == 0
            output = result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            success = False
            output = "Timeout occurred"
    return success, output

def parse_test_cases(test_code):
    try:
        tree = ast.parse(test_code)
        test_cases = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Assert):
                test_expression = ast.unparse(node.test)
                test_cases.append(test_expression)
        return test_cases
    except Exception:
        return []

def calculate_aggregate_coverage_overlap(human_tests_list, generated_tests_list):
    human_test_cases = set()
    generated_test_cases = set()

    for human_tests in human_tests_list:
        human_test_cases.update(parse_test_cases(human_tests))
    for generated_tests in generated_tests_list:
        generated_test_cases.update(parse_test_cases(generated_tests))

    if not human_test_cases:
        return 0  

    overlap = human_test_cases & generated_test_cases
    return (len(overlap) / len(human_test_cases)) * 100

def evaluate_clarity(generated_tests_list):

    total_score = 0
    for generated_tests in generated_tests_list:
        if not generated_tests:
            continue
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_file:
            temp_file.write(generated_tests)
            temp_file.flush()
            try:
                result = subprocess.run(
                    ["pylint", temp_file.name],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                output = result.stdout
                for line in output.split("\n"):
                    if "Your code has been rated at" in line:
                        score = line.split(" ")[-1].split("/")[0]
                        total_score += float(score)
            except Exception:
                pass  # Ignore failed evaluations
    return total_score / len(generated_tests_list) if generated_tests_list else 0

def test_generation_with_tool(dataset_path):
    human_tests_list = []
    generated_tests_list = []
    total_passed = 0
    total_tasks = 0

    with open(dataset_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= 50:  
                break
            problem = json.loads(line)
            total_tasks += 1

            canonical_solution = problem['canonical_solution']
            human_tests = problem['test']
            human_tests_list.append(human_tests)

            generated_tests, _ = generate_tests_with_tool(canonical_solution)
            generated_tests_list.append(generated_tests)

            if generated_tests:
                success, _ = run_generated_tests(canonical_solution, generated_tests)
                if success:
                    total_passed += 1

    pass_rate = (total_passed / total_tasks) * 100
    coverage_overlap = calculate_aggregate_coverage_overlap(human_tests_list, generated_tests_list)
    clarity_score = evaluate_clarity(generated_tests_list)

    return {
        "Total Tasks": total_tasks,
        "Pass Rate": pass_rate,
        "Coverage Overlap": coverage_overlap,
        "Clarity Score": clarity_score,
    }

dataset_path = 'human-eval-v2-20210705.jsonl'
metrics = test_generation_with_tool(dataset_path)

for key, value in metrics.items():
    print(f"{key}: {value:.2f}%")
