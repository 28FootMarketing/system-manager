
import streamlit as st
import datetime
from utils.bill_logic import run_ops, check_ai_status, push_alerts, download_report
import pytz  # If using Python < 3.9
from bill_config import get_current_est_time
from bill_alerts import get_recent_alerts, filter_alerts_by_agent, clear_alerts


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
if st.sidebar.button("🔍 View Alerts", key="view_alerts_btn"):
    show_alerts()
    
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

# Alert Clearing
if st.sidebar.button("🧹 Clear All Alerts"):
    st.success(clear_alerts())


# Main content - Alert Display
st.markdown("### 🔔 Recent Alerts")

agent_filter = st.text_input("Filter alerts by agent name (case-sensitive):")

if agent_filter:
    filtered_alerts = filter_alerts_by_agent(agent_filter)
    if filtered_alerts:
        for alert in reversed(filtered_alerts):
            st.error(f"[{alert['timestamp']}] {alert['agent']}: {alert['message']}")
    else:
        st.info("No alerts found for this agent.")
else:
    recent_alerts = get_recent_alerts()
    if recent_alerts:
        for alert in reversed(recent_alerts):
            st.error(f"[{alert['timestamp']}] {alert['agent']}: {alert['message']}")
    else:
        st.success("✅ No recent alerts logged.")

# === Alert Management Section ===
st.sidebar.markdown("### 🛑 System Alerts")

# Agent filter dropdown
selected_agent = st.sidebar.selectbox(
    "Filter alerts by agent",
    ["All"] + ["Kobe", "Lisa", "Maya", "Magic", "Dawn", "Ebony", "Reggie", "Serena", "Alexis", "Kaiyon"]
)

# Display alerts
alerts_to_show = (
    get_recent_alerts() if selected_agent == "All"
    else filter_alerts_by_agent(selected_agent)
)

for alert in alerts_to_show:
    st.sidebar.warning(f"[{alert['timestamp']}] {alert['agent']}: {alert['message']}")

# Clear button
if st.sidebar.button("🧹 Clear All Alerts", key="clear_alerts_btn"):
    clear_alerts()
    st.sidebar.success("All alerts cleared.")
