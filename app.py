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

# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "services.json"), "r") as f:
    services = json.load(f)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* REMOVE DEFAULT GAP */
.block-container {
    padding-top: 0rem;
}

/* HEADER */
.header {
    background-color: #0A2A66;
    padding: 25px 20px 35px;
    border-radius: 0 0 22px 22px;
}

/* CENTER TEXT */
.center-text {
    text-align: center;
    color: white;
}

/* SATYAMEV */
.satyamev {
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 8px;
}

/* APP NAME */
.app-name {
    font-size: 32px;
    font-weight: 800;
    margin: 0;
}

/* SUBTEXT */
.subtext {
    font-size: 14px;
    opacity: 0.95;
}

/* TAGLINE */
.tagline {
    font-weight: 600;
    margin-top: 6px;
}

/* TIRANGA LINE */
.tiranga {
    margin: 14px auto 0;
    width: 140px;
    height: 4px;
    background: linear-gradient(
        to right,
        #FF9933 0%,
        #FF9933 33%,
        white 33%,
        white 66%,
        #138808 66%,
        #138808 100%
    );
    border-radius: 6px;
}

/* WHITE CONTENT */
.content {
    background: white;
    padding: 28px;
    border-radius: 20px;
    margin-top: -12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}

/* CARDS */
.card {
    background: #f8f9fa;
    padding: 18px;
    border-left: 5px solid #0A2A66;
    border-radius: 12px;
    margin-top: 15px;
}

/* FOOTER */
.footer {
    text-align: center;
    font-size: 12px;
    color: gray;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGO ROW ----------------
col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.image("logo.png.jpeg", width=90)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <div class="center-text">
        <div class="satyamev">सत्यमेव जयते</div>
        <div class="app-name">GovGuide AI</div>
        <div class="subtext">Your trusted guide for Government Services</div>
        <div class="tagline">Towards a Corruption-Free, Informed India 🇮🇳</div>
        <div class="tiranga"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTENT ----------------
st.markdown("<div class='content'>", unsafe_allow_html=True)

user_input = st.text_input(
    "🔍 Search Government Service",
    placeholder="PAN Card, Aadhaar, Passport"
)

def normalize(text):
    return text.lower().strip()

normalized_services = {normalize(k): v for k, v in services.items()}

if user_input:
    service = normalized_services.get(normalize(user_input))

    if service:
        st.markdown("<div class='card'><b>📄 Required Documents</b></div>", unsafe_allow_html=True)
        for doc in service["documents"]:
            st.write(f"• {doc}")

        st.markdown("<div class='card'><b>🌐 Official Website</b></div>", unsafe_allow_html=True)
        st.write(service["official_link"])

        choice = st.radio(
            "How do you want to apply?",
            ["Self (Recommended)", "Using Agent"]
        )

        if choice == "Self (Recommended)":
            st.markdown("<div class='card'><b>📝 Steps to Apply</b></div>", unsafe_allow_html=True)
            for step in service["steps"]:
                st.write(f"• {step}")
        else:
            charge = st.number_input("Agent charge (₹)", min_value=0)
            if charge <= service["official_cost"] * 2:
                st.success("✅ Charge looks reasonable")
            else:
                st.error("❌ Possible overcharging detected")

        if st.button("🤖 Explain in simple language"):
            with st.spinner("AI is explaining..."):
                explanation = get_gemini_response(
                    f"Explain {user_input} government service in very simple language for a common Indian citizen."
                )
            st.markdown("<div class='card'><b>🧠 AI Explanation</b></div>", unsafe_allow_html=True)
            st.write(explanation)

    else:
        st.info("Service not found.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
GovGuide AI is for guidance only.  
We are not affiliated with any Government authority.
</div>
""", unsafe_allow_html=True)
