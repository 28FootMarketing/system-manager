
import streamlit as st
import datetime
from utils.bill_logic import run_ops, check_ai_status, push_alerts, download_report
import pytz  # If using Python < 3.9
download_report
from bill_config import get_current_est_time

st.set_page_config(page_title="Bill - System Monitor", layout="wide")

# Set up the page
st.set_page_config(page_title="Bill: The General | Facilitate The Process", layout="wide")

st.title("🎖️ Bill - The General")
st.subheader("Business Operations Control Panel")
st.markdown("Welcome back, Commander. Your daily mission brief is below:")

# Set timezone to Eastern
eastern = pytz.timezone('US/Eastern')
now_est = datetime.datetime.now(eastern)

# Streamlit display
st.markdown(f"🕒 {now_est.strftime('%A, %B %d, %Y | %I:%M %p')} (EST)")

# Sidebar Toggles
st.sidebar.header("System Commands")
if st.sidebar.button("▶ Run Ops"):
    st.success(run_ops())

if st.sidebar.button("🧪 Check AI Agent Status"):
    st.info(check_ai_status())

if st.sidebar.button("🚨 Simulate Alert"):
    st.warning(push_alerts())

if st.sidebar.button("📥 Download Report"):
    st.info(download_report())

st.markdown("### Logs and Alerts")
st.write("Command outputs will display above based on sidebar interaction.")

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
