import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
cle = os.getenv("Groq_API_KEY")
client = Groq(api_key=cle)

def Resume(text):

    respond = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[
            {'role':'system',
             'content':"fais une resume de texte concis qui capture les idee essentiel, sans detail le superflus." },
             {'role':'user',
              'content':text}
        ]
    )

    return respond.choices[0].message.content


texte = st.text_input("Entre un texte pour te faire une resume")

if st.button('Resume'):
    st.write(Resume(texte))    