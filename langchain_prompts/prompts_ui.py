from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
import os 

load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
st.header('RESEARCH TOOL')

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    elif ChatGoogleGenerativeAI is None:
        st.error("The langchain Google package is not installed. Install the required dependencies first.")
    else:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("GOOGLE_API_KEY is not set. Add it to your environment or .env file.")
        else:
            model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
            result = model.invoke(user_input)
            st.write(getattr(result, "content", result))

       