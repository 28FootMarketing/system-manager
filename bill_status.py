
import json
import os
from datetime import datetime
from bill_config import get_current_est_time

STATUS_FILE = "bill_status.json"

def initialize_status():
    if not os.path.exists(STATUS_FILE):
        status = {
            "last_updated": get_current_est_time(),
            "agent_health": {},
            "active_alerts": [],
            "total_checks": 0,
            "alerts_triggered": 0
        }
        save_status(status)

def load_status():
    with open(STATUS_FILE, "r") as file:
        return json.load(file)

def save_status(status):
    with open(STATUS_FILE, "w") as file:
        json.dump(status, file, indent=4)

def update_agent_status(agent_name, status_data):
    status = load_status()
    status["agent_health"][agent_name] = status_data
    status["last_updated"] = get_current_est_time()
    save_status(status)

def log_alert(agent_name, reason):
    status = load_status()
    status["active_alerts"].append({
        "agent": agent_name,
        "reason": reason,
        "timestamp": get_current_est_time()
    })
    status["alerts_triggered"] += 1
    save_status(status)

def clear_alerts():
    status = load_status()
    status["active_alerts"] = []
    save_status(status)
