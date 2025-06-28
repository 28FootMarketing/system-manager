# bill_alerts.py

import datetime

ALERT_LOG = []

def log_alert(agent_name, alert_message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ALERT_LOG.append({
        "agent": agent_name,
        "message": alert_message,
        "timestamp": timestamp
    })

def get_recent_alerts(limit=10):
    return ALERT_LOG[-limit:]

def clear_alerts():
    ALERT_LOG.clear()
    return "✅ All alerts cleared."
