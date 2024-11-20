import streamlit as st
from processing import initialize_vectorstore, generate_code_assistance_prompt, get_ai_assistance, get_relevant_context
import json
vector_store = initialize_vectorstore()



def main():
    st.set_page_config(layout="wide")
    st.title("LLM Code Assistance Tool with PDF Knowledge Base")

    col1, col2 = st.columns(2)
    with col1:
        task = st.selectbox("Select a task", ["", "Refactor Code", "Generate Tests"])
        language = st.selectbox("Select Language", ["Python", "Java", "JavaScript", "C++", "C#", "HTML", "React", "SQL", "PHP", "R", "Swift"])
        code = st.text_area("Enter your code here", height=300)
        button = st.button("Generate Assistance")

    with col2:
        if button:
            if code and task and language:
                context = get_relevant_context(vector_store, code)
                prompt = generate_code_assistance_prompt(code, task, language, context)
                
                ai_response = get_ai_assistance(prompt, task)
                
                try:
                    response_json = json.loads(ai_response)
                    print(response_json, task)
                    st.success(f"{task} Completed!")

                    if task == "Refactor Code" and "code" in response_json:
                        st.subheader("Refactored Code")
                        st.code(response_json["code"], language=language.lower())
                        st.subheader("Explanation")
                        st.write(response_json["explanation"])

                   
                        
                    if  task == "Generate Tests":
                        st.subheader("Unit Test Suggestions")
                        # Ensure proper handling of code blocks for test cases
                        try:
                            print("response ", response_json["test"])
                            st.code(response_json["test"], language=language.lower())
                        except Exception as e:
                            st.error(f"Error displaying the tests: {e}")
                        
                        # Provide explanation for the tests
                        if "explanation" in response_json:
                            st.subheader("Explanation")
                            st.write(response_json["explanation"])
                        else:
                            st.warning("No explanation provided for the test cases.")

                except json.JSONDecodeError:
                    st.error("Failed to parse the response. Please try again.")
            else:
                st.warning("Please enter your code and select a task before submitting.")

if __name__ == '__main__':
    main()