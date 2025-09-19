import streamlit as sl
import polars  
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
        df1 = polars.read_csv(files[0]).with_columns(polars.col("Roll no").cast(polars.Int64, strict=False))
        df2 = polars.read_csv(files[1]).with_columns(polars.col("Roll no").cast(polars.Int64, strict=False))
        df3 = polars.read_csv(files[2]).with_columns(polars.col("Roll no").cast(polars.Int64, strict=False))
        df2 = df2.drop(["Name","Branch"])
        df3 = df3.drop(["Name", "Branch"])
        merged_df = (df1.join(df2, on="Roll no", how="inner").join(df3, on="Roll no", how="inner"))
        merged_df.write_csv(r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\merged.csv")
        sl.switch_page("pages/data_page.py")

main_page()
