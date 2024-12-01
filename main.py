from flask import Flask, request, jsonify
from flask_cors import CORS
from processing import initialize_vectorstore, generate_code_assistance_prompt, get_ai_assistance, get_relevant_context

app = Flask(__name__)
CORS(app)  

vector_store = initialize_vectorstore(pdf_folder='backend_PDFs')

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        code = data.get("code")
        task = data.get("task")
        language = data.get("language")

        if not code or not task or not language:
            return jsonify({"error": "Missing required fields"}), 400

        context = get_relevant_context(vector_store, code)
        
        prompt = generate_code_assistance_prompt(code, task, language, context)

        response = get_ai_assistance(prompt, task)
        
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)