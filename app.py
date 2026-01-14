import streamlit as st
from gemini_service import get_gemini_response

st.set_page_config(page_title="GovGuide AI", layout="centered")

st.title("🏛️ GovGuide AI")
st.write("Ask anything about Indian government services")

user_input = st.text_input("Enter your question")
if user_input:
    with st.spinner("Thinking..."):
        response = get_gemini_response(user_input)
        st.success(response)
