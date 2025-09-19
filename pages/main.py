import streamlit as sl
import polars as pl
from google import genai 
import requests
from streamlit_lottie import st_lottie

def main_page():
    #setting up the page
    sl.set_page_config(page_title = "EduBud", page_icon = 
                       r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\Code ON.png")
    
    url = "https://lottie.host/15d5fc02-08b4-47ce-b53b-6b18a15787cb/fNZ1Eito8c.json"
    response = requests.get(url)
    animation_json = response.json()
    st_lottie(animation_json, height=300, key="lottie1")
    
    #taking user file input and storing in a dataframe
    files = sl.file_uploader("Upload student data spreadsheets", accept_multiple_files=True,
                              type=None, width="stretch")
    
    
    if len(files) == 3:
        sl.switch_page(r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\pages\data_page.py")

main_page()
