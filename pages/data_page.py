import streamlit as sl
import polars as pl
from streamlit_lottie import st_lottie
import requests
from google import genai

def data_page():
    
    #setting up the page
    sl.set_page_config(page_title = "EduBud: Data", page_icon = 
                       r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\Code ON.png")
    url = "https://lottie.host/53587c86-e5ba-45b2-bed3-5aeb93a73da5/uBfVjhmifJ.json"
    response = requests.get(url)
    animation_json = response.json()
    st_lottie(animation_json, height=300, key="lottie1")

    

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
    if user_input := sl.chat_input("Ask AER about air pollution solutions..."):
        # Store user message
        sl.session_state.messages.append({"role": "user", "content": user_input})
        with sl.chat_message("user"):
            sl.markdown(user_input)
        
        # Get AI response
        with sl.chat_message("assistant"):
            with sl.spinner("Thinking..."):
                response = client.chat_completion(
                model="gemini-2.5-flash", 
                messages=sl.session_state.messages,
                max_tokens=500,
            )
            bot_reply = response.choices[0].message["content"]
            sl.markdown(bot_reply)
            # Store AI reply
            sl.session_state.messages.append({"role": "assistant", "content": bot_reply})

Gemini_api = sl.secrets["gemini_api"]
client = genai.Client(api_key = Gemini_api)
model_id = "gemini-2.5-flash"
