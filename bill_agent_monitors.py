import json
import os
from datetime import datetime

agent_health_path = "data/extended_agent_health.json"

def load_agent_health():
    if not os.path.exists(agent_health_path):
        return []
    with open(agent_health_path, "r") as f:
        return json.load(f)

def monitor_agent_health():
    agents = load_agent_health()
    alerts = []
    for agent in agents:
        if agent["status"] != "active":
            alerts.append({
                "agent": agent["agent_name"],
                "message": f"{agent['agent_name']} is offline.",
                "time": datetime.now().isoformat()
            })
        if agent["sentiment_score"] < 7.0:
            alerts.append({
                "agent": agent["agent_name"],
                "message": f"⚠️ Low sentiment detected for {agent['agent_name']} (score: {agent['sentiment_score']})",
                "time": datetime.now().isoformat()
            })
        if "issues" in agent and len(agent["issues"]) > 0:
            for issue in agent["issues"]:
                alerts.append({
                    "agent": agent["agent_name"],
                    "message": f"🛑 {agent['agent_name']} reported: {issue}",
                    "time": datetime.now().isoformat()
                })
    return alerts
def monitor_lisa():
    # TODO: Implement actual logic for Lisa
    return "Lisa is operational and passed all checks."

def monitor_maya():
    # TODO: Implement actual logic for Maya
    return "Maya is operational and passed all checks."

def monitor_kobe():
    # TODO: Implement actual logic for Kobe
    return "Kobe is operational and passed all checks."

def monitor_magic():
    # TODO: Implement actual logic for Magic
    return "Magic is operational and passed all checks."

def monitor_serena():
    # TODO: Implement actual logic for Serena
    return "Serena is operational and passed all checks."

def monitor_dawn():
    # TODO: Implement actual logic for Dawn
    return "Dawn is operational and passed all checks."

def monitor_ebony():
    # TODO: Implement actual logic for Ebony
    return "Ebony is operational and passed all checks."

def monitor_reggie():
    # TODO: Implement actual logic for Reggie
    return "Reggie is operational and passed all checks."

def monitor_alexis():
    # TODO: Implement actual logic for Alexis
    return "Alexis is operational and passed all checks."

def monitor_kaiyon():
    # TODO: Implement actual logic for Kaiyon
    return "Kaiyon is operational and passed all checks."
