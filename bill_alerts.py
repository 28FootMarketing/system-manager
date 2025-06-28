# bill_alerts.py

# Global in-memory alert store
_alerts = []

def get_recent_alerts():
    """Return the last 10 alerts."""
    return _alerts[-10:]

def filter_alerts_by_agent(agent_name):
    """Filter alerts by agent name."""
    return [alert for alert in _alerts if alert.get("agent") == agent_name]

def clear_alerts():
    """Clear all stored alerts."""
    global _alerts
    _alerts = []
    return "All alerts cleared."

def push_alert(agent_name, message):
    """Add a new alert for a specific agent."""
    from datetime import datetime
    _alerts.append({
        "agent": agent_name,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
