import streamlit as st
import json
import os
from gemini_service import get_gemini_response

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GovGuide AI",
    page_icon="🏛️",
    layout="centered"
)

# ---------------- BASE DIR ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "services.json"), "r") as f:
    services = json.load(f)

# ---------------- CUSTOM CSS (BORDER + UI) ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6f8;
}
.block-container {
    border: 2px solid #0b5ed7;
    border-radius: 16px;
    padding: 2rem;
    background-color: white;
    box-shadow: 0 12px 30px rgba(0,0,0,0.12);
}
.title-text {
    text-align: center;
    color: #0b5ed7;
    font-size: 32px;
    font-weight: 700;
}
.subtitle-text {
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}
.card {
    padding: 20px;
    background: #f8f9fa;
    border-left: 5px solid #198754;
    border-radius: 10px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGO + TITLE ----------------
st.image("logo.png", width=80)
st.markdown("<div class='title-text'>GovGuide AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle-text'>Ask anything about Indian Government services</div>",
    unsafe_allow_html=True
)

# ---------------- USER INPUT ----------------
user_input = st.text_input("Enter document name", placeholder="PAN Card")

# ---------------- LOGIC ----------------
if user_input:
    service = services.get(user_input)

    if service:
        st.markdown("<div class='card'><h3>Required Documents</h3></div>", unsafe_allow_html=True)
        for doc in service["documents"]:
            st.write(f"• {doc}")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("<div class='card'><h3>Official Website</h3></div>", unsafe_allow_html=True)
        st.write(service["official_link"])

        st.markdown("<br>", unsafe_allow_html=True)

        choice = st.radio(
            "How do you want to apply?",
            ["Self", "Using Agent"]
        )

        if choice == "Self":
            st.markdown("<div class='card'><h3>Steps to Apply</h3></div>", unsafe_allow_html=True)
            for step in service["steps"]:
                st.write(f"• {step}")

        else:
            charge = st.number_input("Agent charge (₹)", min_value=0)
            if charge <= service["official_cost"] * 2:
                st.success("✅ Charge looks reasonable")
            else:
                st.error("❌ Overcharging detected")

    else:
        st.info("ℹ️ Service not found in database.")

