import streamlit as sl
import polars 
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import smtplib
from google import genai

def data_page():
    
    #setting up the page
    sl.set_page_config(page_title = "EduBud: Data", page_icon = 
                       r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\Code ON.png")
    url = "https://lottie.host/bc577d26-154f-4351-a258-10f73bc918f3/LZXZK5Ce1x.json"
    response = requests.get(url)
    animation_json = response.json()
    st_lottie(animation_json, height=300, key="lottie1")

    df = polars.read_csv(r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\merged.csv")
    df = df.with_columns(
        polars.when((polars.col("Attendance") < 75) | (polars.col("Marks (out of 35)") < 12) | (polars.col("Fees") == 0))
         .then(polars.lit("At Risk"))
         .otherwise(polars.lit("Safe"))
         .alias("Status")
    )
    pd_df = df.to_pandas()

    def highlight_risk(row):
        return ['background-color: #ff4d4d'] * len(row) if row["Status"] == "At Risk" else [''] * len(row)

    styled_df = pd_df.style.apply(highlight_risk, axis=1)
    sl.subheader("Student Data")
    sl.dataframe(styled_df, use_container_width=True, height=400)

    tab1 ,tab2, tab3 = sl.tabs([])

    sl.button("Send student to my mail", on_click="mailto:temestgaming49@gmail.com")
    sl.markdown("---")
    sl.header("Talk To EduBud", width = "stretch")

    if "messages" not in sl.session_state:
        sl.session_state.messages = [
            {"role": "system", "content": 
             "You are EduBud, an AI assistant that helps educators detect and support at-risk students."
             "Focus only on analyzing student data such as attendance, marks, and fees, and provide concise, factual, and actionable insights."
             "Maintain a professional, supportive, and student-first tone at all times."
             "Politely refuse questions unrelated to student performance, retention, or counseling, and remind the user of your purpose."
             "If asked who created you, reply: 'I was created by Daksh Gupta."
            }
        ]

    # Display previous messages
    for msg in sl.session_state.messages[1:]:  # skip system msg
        with sl.chat_message(msg["role"]):
            sl.markdown(msg["content"])
            
    # user input
    if user_input := sl.chat_input("Ask EduBud for guidance on how to reduce these students risk"):
        # Store user message
        sl.session_state.messages.append({"role": "user", "content": user_input})
        with sl.chat_message("user"):
            sl.markdown(user_input)
            prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in sl.session_state.messages])

        
        # Get AI response
        with sl.chat_message("assistant"):
            with sl.spinner("Thinking..."):
                response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt
            )
            assistant_reply = response.text
            sl.markdown(assistant_reply)
            # Store AI reply
            sl.session_state.messages.append({"role": "assistant", "content": assistant_reply})

Gemini_api = sl.secrets["gemini_api"]
client = genai.Client(api_key = Gemini_api)
model_id = "gemini-2.5-flash"

data_page()
