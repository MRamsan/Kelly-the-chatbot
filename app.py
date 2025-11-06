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
if "OPENAI_API_KEY" not in st.secrets:
    st.error("⚠️ Please add your OpenAI API key in Streamlit Secrets (Settings → Secrets).")
else:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # --- User Input ---
    topic = st.text_area("💭 Enter a topic or question for Kelly to write a poem about:")

    if st.button("✨ Generate Poem"):
        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Kelly is composing her reflective poem..."):
                system_prompt = """
You are Kelly, an AI Scientist and Poet.
You write short reflective poems about any topic the user provides.
Style: analytical, poetic, logical, and evidence-aware.
End each poem with a thought-provoking insight.
"""
                user_prompt = f"Write a poem about: {topic}"

                # ✅ New API style (works with openai>=1.0.0)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.8,
                    max_tokens=300
                )

                poem = response.choices[0].message.content.strip()
                st.markdown("### 🎓 Kelly’s Poem:")
                st.markdown(f"_{poem}_")

