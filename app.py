app.py

Member B – Frontend, UX & Deployment Leadapp.py

Member B – Frontend, UX & Deployment Lead

GovGuide AI – Streamlit Frontend

import streamlit as st import json from datetime import datetime

------------------ PAGE CONFIG ------------------

st.set_page_config( page_title="GovGuide AI", page_icon="🏛️", layout="centered" )

------------------ LOAD DATA ------------------

@st.cache_data def load_services(): with open("services.json", "r", encoding="utf-8") as f: return json.load(f)

services_data = load_services()

------------------ HEADER ------------------

st.title("🏛️ GovGuide AI") st.subheader("Your Honest Digital Middleman for Government Services")

st.markdown( """ GovGuide AI helps citizens understand government services clearly, avoid fake agents, and save time & money. """ )

st.divider()

------------------ USER INPUT ------------------

st.markdown("### 🔍 Select a Government Service") service_names = list(services_data.keys()) selected_service = st.selectbox("Choose Service", service_names)

st.markdown("### 💰 Agent Fee (Optional)") agent_fee = st.number_input( "Enter agent fee you were asked to pay (₹)", min_value=0, step=50 )

st.button("🔎 Check Details")

st.divider()

------------------ OUTPUT ------------------

if selected_service: service = services_data[selected_service]

st.markdown(f"## 📄 {selected_service}")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**📑 Documents Required:**")
    for doc in service["documents"]:
        st.write(f"• {doc}")

    st.markdown("**⏱ Processing Time:**")
    st.write(service["time"])

with col2:
    st.markdown("**💸 Official Government Fee:**")
    st.write(f"₹ {service['official_fee']}")

    st.markdown("**🌐 Official Website:**")
    st.write(service["website"])

st.divider()

# ------------------ FRAUD CHECK ------------------
st.markdown("### ⚠️ Agent Fee Analysis")

if agent_fee == 0:
    st.info("No agent fee entered. This service can be done directly via official channels.")
else:
    if agent_fee > service["official_fee"]:
        st.error(
            f"🚨 Possible Fraud Detected!\n\n"
            f"Official fee is ₹{service['official_fee']}, but agent asked ₹{agent_fee}."
        )
    else:
        st.success("✅ Agent fee seems reasonable based on official charges.")

------------------ FOOTER ------------------

st.divider() st.caption( f"GovGuide AI | Built for TechSprint | {datetime.now().year}" )

GovGuide AI – Streamlit Frontend

import streamlit as st import json from datetime import datetime

------------------ PAGE CONFIG ------------------

st.set_page_config( page_title="GovGuide AI", page_icon="🏛️", layout="centered" )

------------------ LOAD DATA ------------------

@st.cache_data def load_services(): with open("services.json", "r", encoding="utf-8") as f: return json.load(f)

services_data = load_services()

------------------ HEADER ------------------

st.title("🏛️ GovGuide AI") st.subheader("Your Honest Digital Middleman for Government Services")

st.markdown( """ GovGuide AI helps citizens understand government services clearly, avoid fake agents, and save time & money. """ )

st.divider()

------------------ USER INPUT ------------------

st.markdown("### 🔍 Select a Government Service") service_names = list(services_data.keys()) selected_service = st.selectbox("Choose Service", service_names)

st.markdown("### 💰 Agent Fee (Optional)") agent_fee = st.number_input( "Enter agent fee you were asked to pay (₹)", min_value=0, step=50 )

st.button("🔎 Check Details")

st.divider()

------------------ OUTPUT ------------------

if selected_service: service = services_data[selected_service]

st.markdown(f"## 📄 {selected_service}")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**📑 Documents Required:**")
    for doc in service["documents"]:
        st.write(f"• {doc}")

    st.markdown("**⏱ Processing Time:**")
    st.write(service["time"])

with col2:
    st.markdown("**💸 Official Government Fee:**")
    st.write(f"₹ {service['official_fee']}")

    st.markdown("**🌐 Official Website:**")
    st.write(service["website"])

st.divider()

# ------------------ FRAUD CHECK ------------------
st.markdown("### ⚠️ Agent Fee Analysis")

if agent_fee == 0:
    st.info("No agent fee entered. This service can be done directly via official channels.")
else:
    if agent_fee > service["official_fee"]:
        st.error(
            f"🚨 Possible Fraud Detected!\n\n"
            f"Official fee is ₹{service['official_fee']}, but agent asked ₹{agent_fee}."
        )
    else:
        st.success("✅ Agent fee seems reasonable based on official charges.")

------------------ FOOTER ------------------

st.divider() st.caption( f"GovGuide AI | Built for TechSprint | {datetime.now().year}" )
