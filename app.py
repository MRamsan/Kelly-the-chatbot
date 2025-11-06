# app.py
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.set_page_config(page_title="Kelly - The AI Scientist Poet", page_icon="🤖📜")
st.title("🤖 Kelly — The AI Scientist Poet")

st.write("""
*Ask Kelly about anything — science, art, AI, or human nature.*  
She will respond with a **poem**: skeptical, analytical, and beautifully reasoned.
""")
user_input = st.text_area("💭 Ask Kelly a question or give any topic for poetic analysis:")

if st.button("💬 Ask Kelly"):
    if user_input.strip() == "":
        st.warning("Please enter a topic or question for Kelly.")
    else:
        with st.spinner("Kelly is composing her analytical poem..."):
            prompt = f"""
You are Kelly, an AI Scientist and Poet.
Respond to the user's topic or question in the form of a poem.
Tone: skeptical, analytical, and professional.
Style: poetic, reflective, and grounded in evidence and reason.
Question broad claims, highlight possible limitations,
and end with a practical, evidence-based insight.
User topic: {user_input}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",  # or gpt-4-turbo if available
                messages=[
                    {"role": "system", "content": "You are Kelly, the AI Scientist Poet."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=300
            )

            poem = response.choices[0].message.content.strip()

            st.markdown("### 🎓 Kelly’s Response:")
            st.markdown(f"_{poem}_")


