
import streamlit as st
import datetime
from utils.logic import run_ops, check_ai_status, push_alerts, download_report

# Set up the page
st.set_page_config(page_title="Bill: The General | Facilitate The Process", layout="wide")

st.title("🎖️ Bill - The General")
st.subheader("Business Operations Control Panel")
st.markdown("Welcome back, Commander. Your daily mission brief is below:")

# Date and time display
st.markdown(f"🕒 {datetime.datetime.now().strftime('%A, %B %d, %Y | %I:%M %p')}")

# Action Buttons
if st.button("🛠️ Run Ops"):
    run_ops()

if st.button("📊 Check AI Agent Status"):
    check_ai_status()

if st.button("🚨 Push Team Alerts"):
    push_alerts()

if st.button("🧾 Download Weekly Report"):
    download_report()

st.info("Bill manages your backend systems, automation checks, and agent alerts.")
