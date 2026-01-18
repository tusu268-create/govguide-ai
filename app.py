import streamlit as st
import json
import os
from gemini_service import get_gemini_response

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🏛️GovGuide AI",
    page_icon="🏛️",
    layout="centered"
)

# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "services.json"), "r") as f:
    services = json.load(f)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f4f6f8;
}
.block-container {
    border: 2px solid #0b5ed7;
    border-radius: 18px;
    padding: 2rem;
    background-color: white;
    box-shadow: 0 14px 35px rgba(0,0,0,0.15);
}
.hero-title {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
    color: #0b5ed7;
}
.hero-sub {
    text-align: center;
    color: #555;
    margin-bottom: 10px;
}
.tagline {
    text-align: center;
    font-size: 16px;
    font-weight: 600;
    color: #198754;
    margin-bottom: 30px;
}
.card {
    padding: 20px;
    background: #f8f9fa;
    border-left: 6px solid #198754;
    border-radius: 12px;
    margin-top: 15px;
}
.warning {
    padding: 15px;
    background: #fff3cd;
    border-left: 6px solid #ffc107;
    border-radius: 10px;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 12px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.image("logo.png.jpeg", width=150)
st.markdown("<div class='hero-title'>🏛️GovGuide AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-sub'>Your trusted AI guide for Indian Government services.<br>"
    "No confusion. No fraud. No middlemen.</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div class='tagline'>🇮🇳 Towards a Corruption-Free, Informed India</div>",
    unsafe_allow_html=True
)

# ---------------- SEARCH INPUT ----------------
user_input = st.text_input(
    "🔍 Search Government Service or Document",
    placeholder="Example: PAN Card, Aadhaar, Passport"
)

# ---------------- NORMALIZE INPUT ----------------
def normalize(text):
    return text.lower().strip()

normalized_services = {normalize(k): v for k, v in services.items()}

# ---------------- MAIN LOGIC ----------------
if user_input:
    service = normalized_services.get(normalize(user_input))

    if service:
        st.markdown("<div class='card'><h3>📄 Required Documents</h3></div>", unsafe_allow_html=True)
        for doc in service["documents"]:
            st.write(f"• {doc}")

        st.markdown("<div class='card'><h3>🌐 Official Government Website</h3></div>", unsafe_allow_html=True)
        st.write(service["official_link"])

        st.markdown("<div class='card'><h3>🧭 How do you want to apply?</h3></div>", unsafe_allow_html=True)
        choice = st.radio("", ["Self (Recommended)", "Using Agent"])

        if choice == "Self (Recommended)":
            st.markdown("<div class='card'><h3>📝 Step-by-Step Process</h3></div>", unsafe_allow_html=True)
            for step in service["steps"]:
                st.write(f"• {step}")

        else:
            st.markdown(
                "<div class='warning'><b>⚠️ Anti-Fraud Check</b><br>"
                "This feature protects citizens from overcharging agents.</div>",
                unsafe_allow_html=True
            )

            charge = st.number_input("Enter agent charge (₹)", min_value=0)
            if charge <= service["official_cost"] * 2:
                st.success("✅ Charge looks reasonable")
            else:
                st.error("❌ Possible fraud detected: Overcharging")

        # ---------------- AI EXPLAINER ----------------
        if st.button("🤖 Explain this service in simple language"):
            with st.spinner("AI is explaining..."):
                explanation = get_gemini_response(
                    f"Explain {user_input} government service in very simple language for a common Indian citizen."
                )
            st.info(explanation)

    else:
        st.info("ℹ️ Service not found. Try another government service.")

# ---------------- FOOTER ----------------
st.markdown("""
<div class='footer'>
⚠️ Disclaimer: GovGuide AI provides informational guidance only.  
We are not affiliated with any government authority.
</div>
""", unsafe_allow_html=True)
