from flask import Flask, request, jsonify
from flask_cors import CORS
from processing import initialize_vectorstore, generate_code_assistance_prompt, get_ai_assistance, get_relevant_context

app = Flask(__name__)
CORS(app)  

# Lazy initialization with error handling
try:
    vector_store = initialize_vectorstore(pdf_folder='backend_PDFs')
except Exception as e:
    print(f"Failed to initialize vector store: {e}")
    vector_store = None  # Handle this appropriately in your app

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        # Parse and validate input
        data = request.json
        code = data.get("code")
        task = data.get("task")
        language = data.get("language")

        if not all([code, task, language]):
            return jsonify({"error": "Missing required fields: 'code', 'task', or 'language'"}), 400

        if not isinstance(code, str) or not isinstance(task, str) or not isinstance(language, str):
            return jsonify({"error": "Invalid input types. 'code', 'task', and 'language' must be strings."}), 400

        if not vector_store:
            return jsonify({"error": "Vector store is not initialized. Please contact the administrator."}), 500

        # Generate prompt
        context = get_relevant_context(vector_store, code)
        prompt = generate_code_assistance_prompt(code, task, language, context)

        # Get AI assistance
        response = get_ai_assistance(prompt, task)

        return jsonify({"response": response})
    except Exception as e:
        # Log the exception for debugging
        print(f"Error in /api/generate: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
