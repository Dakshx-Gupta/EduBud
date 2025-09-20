import streamlit as sl
import polars
from streamlit_lottie import st_lottie
import requests
import smtplib
from google import genai

def data_page():

    sl.set_page_config(page_title="EduBud: Data", 
                       page_icon=r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\Code ON.png")
    sl.title("📊Data")

    # Lottie animation
    url = "https://lottie.host/bc577d26-154f-4351-a258-10f73bc918f3/LZXZK5Ce1x.json"
    response = requests.get(url)
    animation_json = response.json()
    st_lottie(animation_json, height=300, key="lottie1")

    df = polars.read_csv(r"C:\Users\tempe\OneDrive\Documents\EduBud\EduBud\merged.csv")
    df = df.with_columns(
        polars.when(
            (polars.col("Attendance") < 75) | 
            (polars.col("Marks (out of 35)") < 12) | 
            (polars.col("Fees") == 0)
        )
        .then(polars.lit("At Risk"))
        .otherwise(polars.lit("Safe"))
        .alias("Status")
    )
    pd_df = df.to_pandas()  # for Streamlit

    tab1, tab2, tab3 = sl.tabs(["📊 Dashboard", "🔍 Student Search", "📈 Insights"])


    with tab1:
        sl.subheader("Student Data")

        def highlight_risk(row):
            return ['background-color: #ff4d4d'] * len(row) if row["Status"] == "At Risk" else [''] * len(row)

        styled_df = pd_df.style.apply(highlight_risk, axis=1)
        sl.dataframe(styled_df, use_container_width=True, hide_index=True)
        csv_data = df.write_csv()

        sl.download_button("📩 Download data", data = csv_data, file_name="merged.csv")

    with tab2:
        sl.subheader("Search Student by Roll No")
        roll_input = sl.text_input("Enter Roll No")
        if roll_input:
            student = pd_df[pd_df["Roll no"].astype(str) == str(roll_input)]
            if not student.empty:
                sl.success(f"🎯 Profile Found for Roll No {roll_input}")
                sl.table(student.reset_index(drop=True))

                status = student.iloc[0]["Status"]
                if status == "At Risk":
                    sl.error("⚠ This student is At Risk!")
                else:
                    sl.success("✅ This student is Safe")

                perf = student.melt(
                    id_vars=["Roll no", "Name"], 
                    value_vars=["Attendance", "Marks (out of 35)", "Fees"]
                )
                perf = perf.set_index("variable")["value"]
                sl.bar_chart(perf)

            else:
                sl.warning("No student found with that Roll No.")

    with tab3:
        sl.subheader("Visual Insights")

        sl.write("### Attendance vs Marks")
        scatter_data = pd_df[["Attendance", "Marks (out of 35)"]]
        sl.line_chart(scatter_data)

        sl.write("### Fee Payment Status")
        fee_counts = pd_df["Fees"].value_counts()
        sl.bar_chart(fee_counts)

        sl.write("### Branch-wise Risk Status")
        branch_counts = pd_df.groupby(["Branch", "Status"]).size().unstack(fill_value=0)
        sl.bar_chart(branch_counts)

    sl.markdown("---")
    sl.header("💬 Talk To EduBud")

    if "messages" not in sl.session_state:
        sl.session_state.messages = [
            {"role": "system", "content":
             "You are EduBud, an AI assistant that helps educators detect and support at-risk students."
             "Focus only on analyzing student data such as attendance, marks, and fees, and provide concise, factual, and actionable insights."
             "Maintain a professional, supportive, and student-first tone at all times."
             "Politely refuse questions unrelated to student performance, retention, or counseling, and remind the user of your purpose."
             "If asked who created you, reply: 'I was created by Daksh Gupta.'"
            }
        ]

    # Display previous messages
    for msg in sl.session_state.messages[1:]:  # skip system msg
        with sl.chat_message(msg["role"]):
            sl.markdown(msg["content"])

    # user input
    if user_input := sl.chat_input("Ask EduBud for guidance on how to reduce student risk"):
        sl.session_state.messages.append({"role": "user", "content": user_input})
        with sl.chat_message("user"):
            sl.markdown(user_input)
            prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in sl.session_state.messages])

        with sl.chat_message("assistant"):
            with sl.spinner("Thinking..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=prompt
                )
            assistant_reply = response.text
            sl.markdown(assistant_reply)
            sl.session_state.messages.append({"role": "assistant", "content": assistant_reply})

Gemini_api = sl.secrets["gemini_api"]
client = genai.Client(api_key=Gemini_api)
model_id = "gemini-2.5-flash"

data_page()