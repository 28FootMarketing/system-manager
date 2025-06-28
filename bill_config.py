
import pytz
from datetime import datetime

# Timezone
EASTERN_TIMEZONE = pytz.timezone('US/Eastern')

# Logging and alert settings
ALERT_THRESHOLD = 2  # Number of failed checks before alert triggers
MONITOR_INTERVAL_MINUTES = 15

# List of agents Bill should monitor
MONITORED_AGENTS = [
    'Kobe', 'Lisa', 'Maya', 'Magic', 'Dawn',
    'Ebony', 'Reggie', 'Cheryl', 'Allen', 'Kaiyon',
    'Alexis', 'Serena'
]

# Notification settings
ADMIN_EMAIL = 'admin@facilitatetheprocess.com'
ADMIN_SMS = '+14445556666'

# System status keys
SYSTEM_STATUS = {
    'last_check': None,
    'active_alerts': [],
    'monitored': MONITORED_AGENTS,
    'alerts_enabled': True
}

# Utility to get current EST time
def get_current_est_time():
    return datetime.now(EASTERN_TIMEZONE).strftime('%A, %B %d, %Y | %I:%M %p')
