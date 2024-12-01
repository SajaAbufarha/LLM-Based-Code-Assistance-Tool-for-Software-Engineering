import matplotlib.pyplot as plt
import json
import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

generated_tests_file = "generated_tests_evaluation.json"
refactored_code_file = "refactored_code_evaluation.json"

generated_tests_data = load_data(generated_tests_file)
refactored_code_data = load_data(refactored_code_file)

data = {
    "Generated Tests": {
        "Total Correctness Score": generated_tests_data["Total Correctness Score"],
        "Average Code Correctness": generated_tests_data["Average Code Correctness"]
    },
    "Refactored Code": {
        "Total Correctness Score": refactored_code_data["Total Correctness Score"],
        "Average Code Correctness": refactored_code_data["Average Code Correctness"]
    },
}

categories = list(data.keys())
total_correctness_scores = [data[cat]["Total Correctness Score"] for cat in categories]
average_code_correctness = [data[cat]["Average Code Correctness"] for cat in categories]

bar_width = 0.35

x = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(x - bar_width / 2, total_correctness_scores, bar_width, label="Total Correctness Score")
bar2 = ax.bar(x + bar_width / 2, average_code_correctness, bar_width, label="Average Code Correctness (%)")

ax.set_xlabel("Evaluation Type", fontsize=12)
ax.set_ylabel("Scores", fontsize=12)
ax.set_title("Comparison of Total and Average Code Correctness", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=11)
ax.legend(fontsize=11)

for bar in bar1 + bar2:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f"{height:.1f}", ha="center", fontsize=10)

plt.tight_layout()
plt.show()
