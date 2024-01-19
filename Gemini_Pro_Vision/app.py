from api_key import GOOGLE_API_KEY
import google.generativeai as genai
import streamlit as st
from PIL import Image


# Initializing GoogleGEMINI Api_KEY
genai.configure(api_key=GOOGLE_API_KEY)


# functions for getting respnse from LLM Model
def get_response(input,img):
     model = genai.GenerativeModel(model_name='gemini-pro-vision')
     if input!='':
          response = model.generate_content([input,img])
     else:
          response = model.generate_content(img)
     return response.text



# Initializing Streamlit app
st.set_page_config(page_title='Q&A with Images')

st.header('Gemini Applications')

# taking input from user
input = st.text_input('Input: ',key='input')
# taking image file from user
upload_file = st.file_uploader('Upload Image : ',type=['jpeg','png','jpg'])
image = ""

# uploading an image
if upload_file is not None:
     img = Image.open(upload_file)
     st.image(img,caption='Uploaded image',use_column_width=True)

btn = st.button('Generate Content')



# finally throw result by this below code
if btn:
     response = get_response(input,img)
     st.subheader('Your Result')
     st.write(response)
     


