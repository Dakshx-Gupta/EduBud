import streamlit as st
import polars as pl
from google import genai 

Gemini_api = st.secrets["gemini_api"]

client = genai.Client(api_key = Gemini_api)
response = client.models.generate_content(
    model="gemini-2.5-flash", contents= "Explain AI"
)
print(response.text)
