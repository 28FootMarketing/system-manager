import json
import os
from datetime import datetime

def push_alerts(new_alerts):
    for alert in new_alerts:
        if "timestamp" not in alert:
            alert["timestamp"] = datetime.now().isoformat()
    existing = get_recent_alerts()
    combined = existing + new_alerts
    with open(alerts_file_path, "w") as f:
        json.dump(combined, f, indent=2)
alerts_file_path = "alerts.json"

# ✅ Ensure alerts.json exists and is readable
def ensure_alerts_file():
    if not os.path.exists(alerts_file_path):
        with open(alerts_file_path, "w") as f:
            json.dump([], f)
    else:
        try:
            with open(alerts_file_path, "r") as f:
                json.load(f)
        except (json.JSONDecodeError, IOError):
            # Recreate a clean file if corrupted
            with open(alerts_file_path, "w") as f:
                json.dump([], f)

# 🧠 Load alerts
def get_recent_alerts():
    ensure_alerts_file()
    with open(alerts_file_path, "r") as f:
        return json.load(f)
def push_alerts(new_alerts):
    existing = get_recent_alerts()
    combined = existing + new_alerts
    with open(alerts_file_path, "w") as f:
        json.dump(combined, f, indent=2)
# 🔍 Filter alerts by agent
def filter_alerts_by_agent(agent_name):
    alerts = get_recent_alerts()
    return [alert for alert in alerts if alert.get("agent") == agent_name]

# 🧹 Clear all alerts
def clear_alerts():
    ensure_alerts_file()  # optional safeguard
    with open(alerts_file_path, "w") as f:
        json.dump([], f)

