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

topic = st.text_area("Enter a topic or question for Kelly:")

if st.button("Ask Kelly"):
    if topic.strip():
        system_prompt = """
        You are Kelly, the AI Scientist Poet.
        You must respond ONLY in the form of a poem.
        Every poem should sound skeptical, analytical, and professional in tone.
        You question broad claims, reveal limitations, and end with a practical, evidence-based insight.
        Write in the style of a reflective scientist-poet — logical yet lyrical.
        """

        user_prompt = f"Write a poem about: {topic}"

        # ✅ New API style
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4-turbo" if available
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )

        poem = response.choices[0].message.content
        st.markdown(f"### Kelly’s Poem on *{topic.title()}* ✨")
        st.markdown(poem)
    else:
        st.warning("Please enter a topic for Kelly to write about.")

