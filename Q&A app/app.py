# Import Libraries
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai


# load env variables
load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")

# config api key
genai.configure(api_key=gemini_api_key)



# define function for LLMModel

def LLMModel(user):
     model = genai.GenerativeModel(model_name="gemini-pro")
     
     if user:
          response = model.generate_content(user)
     else:
          response = st.error('Invalid Input')

     return response.text




# Frontend

st.set_page_config(page_title="Q&A")

st.header("Q&A Application")

user_input = st.text_input('Enter: ')

btn = st.button("Ask")

if btn:
     if user_input:
          with st.spinner():
               result = LLMModel(user_input)
               st.write(result)
               st.success('Success')
     else:
          st.error("Enter Input")
