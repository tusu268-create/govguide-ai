import streamlit as st
import json
import os
from gemini_service import get_gemini_response
st.image("logo.png.jpeg", width=150)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "services.json"), "r") as f:
    services = json.load(f)

st.title("🏛️GovGuide AI")
st.write("Ask anything about Indian Government services")

user_input = st.text_input("Enter document name (e.g. PAN Card)")

if user_input:
    service = services.get(user_input)

    if service:
        
        st.subheader("Required Documents")
        for doc in service["documents"]:
            st.write(f"- {doc}")

        st.subheader("Official Website")
        st.write(service["official_link"])

        choice = st.radio(
            "How do you want to apply?",
            ["Self", "Using Agent"]
        )

        if choice == "Self":
            st.subheader("Steps to Apply")
            for step in service["steps"]:
                st.write(f"- {step}")

        else:
            charge = st.number_input("Agent charge (₹)", min_value=0)
            if charge <= service["official_cost"] * 2:
                st.success("✅ Charge looks reasonable")
            else:
                st.error("❌ Overcharging detected")

    else:
        st.info("Service not found in database.")
