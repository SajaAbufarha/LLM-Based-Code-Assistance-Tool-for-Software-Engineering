import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import openai
from langchain_community.document_loaders import PyPDFLoader
from typing import List
import fitz
import json
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

SYSTEM_PROMPT = """You are a helpful assistant for software engineers. 
You are given textbooks that outline foundational principles for code testing, refactoring, and other essential practices. 
Use the textbooks as a guide for providing feedback that is both grounded in these principles and specifically tailored to the given code.

Key Guidelines:
- Use textbook principles solely as inspiration or guidelines for your tests or refactored code.
- Do not refer to any specific examples or cases within the textbooks; instead, focus only on broad principles.

"""

def load_pdfs_from_backend(folder_path: str) -> List[str]:
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            pdf_text = ""
            with fitz.open(file_path) as pdf:  
                for page in pdf:
                    pdf_text += page.get_text()  
            documents.append(pdf_text)  
    return documents

def get_text_chunks(documents: List[str], chunk_size: int = 500) -> List[str]:
    chunks = []
    for doc in documents:
        doc_chunks = [doc[i:i + chunk_size] for i in range(0, len(doc), chunk_size)]
        chunks.extend(doc_chunks)
    return chunks

def get_vectorstore(chunks: List[str]):
    embedding = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(chunks, embedding)
    return vector_store

def initialize_vectorstore(pdf_folder='backend_PDFs'):
    documents = load_pdfs_from_backend(pdf_folder)
    chunks = get_text_chunks(documents)
    vector_store = get_vectorstore(chunks)
    return vector_store

def generate_code_assistance_prompt(code, task, language="Python", context=None):
    if task == "Refactor Code":
        prompt = f"""
            The following is a {language} code snippet:
                {code}
                Refactor the code to improve readability and maintainability               
                Please provide your response in JSON format as shown below:
            {{
                "code": "Refactored code with inline comments",
                "explanation": "High-level explanation of code changes or improvements"
            }}
            """
            
  
        
        
    elif task == "Generate Tests":
        prompt =  f"""
            The following is a {language} code snippet:
                {code}
                Please write unit tests for the above code to ensure its proper functioning 
                               
                Please provide your response in JSON format as shown below:
            {{
                "tests": "Unit tests checking the behavior of individual units of code in isolation",
                "explanation": "High-level explanation of code changes or improvements"
            }}
            """
    else:
        prompt += "Invalid task selected."
        
        
    if context:
        prompt += f"\n\nThe context to guide your response is:\n{context}"
        
    return prompt

def get_ai_assistance(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]
        )
        response = completion['choices'][0]['message']['content']
        print("Raw AI Response:\n", response)  # debug
        return response
    except Exception as e:
        print("Error in AI Assistance:", str(e))
        return f"Error: {str(e)}"

def get_relevant_context(vector_store, code, top_k=3):
    relevant_docs = vector_store.similarity_search(code, k=top_k)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    return context
