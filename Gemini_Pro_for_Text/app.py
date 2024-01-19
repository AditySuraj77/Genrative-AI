import google.generativeai as genai
from api_key import GOOGLE_API_KEY
import streamlit as st



genai.configure(api_key=GOOGLE_API_KEY)

def Genaimodel(question):
     model = genai.GenerativeModel(model_name='gemini-pro')
     response = model.generate_content(question)
     return response.text





st.set_page_config(page_title='Q&A')

st.header("Gemini LLM Applications")

input = st.text_input('Input: ',key='input')


bttn = st.button('Chat')



if bttn:
     result = Genaimodel(input)
     st.subheader('Your Result')
     st.write(result)

