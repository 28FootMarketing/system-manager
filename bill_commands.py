def assign_task(command):
    try:
        _, name, _, task = command.split(maxsplit=3)
        return f"✅ Assigned {name} to task: '{task}'"
    except:
        return "❌ Usage: /assign [name] to [task]"

def start_monitoring(command):
    try:
        parts = command.split()
        name = parts[1]
        duration = parts[3]
        return f"📊 Monitoring {name} for {duration}"
    except:
        return "❌ Usage: /monitor [agent_name] for [duration]"

def audit_agent(command):
    try:
        name = command.split()[1]
        return f"🔍 Audit initiated for agent: {name}"
    except:
        return "❌ Usage: /audit [agent_name] now"

def reload_agents():
    return "🔄 Agents reloaded."

def toggle_agent(command):
    try:
        _, name, status = command.split()
        if status not in ['on', 'off']:
            raise ValueError
        return f"🔁 {name} turned {status}"
    except:
        return "❌ Usage: /toggle [agent_name] [on/off]"

def simulate_alert(command):
    try:
        agent_name = command.split()[-1]
        return f"🚨 Simulated alert from {agent_name}"
    except:
        return "❌ Usage: /simulate alert from [agent_name]"

def reset_memory(command):
    try:
        agent_name = command.split()[-1]
        return f"♻️ Memory reset for {agent_name}"
    except:
        return "❌ Usage: /reset agent memory [agent_name]"
