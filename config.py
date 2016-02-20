
#=========
# CONTROL
#=========

# (STR) WLAN interface to use - run.sh puts into monitor mode.
#       If this is blank, run.sh will use first wlan interface.
IFACE = 'wlan1'

# (LIST) List of MAC addresses expected within the premises
MAC_LIST = [
    'xx:xx:xx:xx:xx:xx',
    'xx:xx:xx:xx:xx:xx',
    ]

# (STR) Vendor name to report for probes from Local Admin MAC addresses
ADMIN_OUI = 'Admin OUI'

# (BOOL) Automatically white list Local Admin MAC addresses
# WARNING...
# iOS MAC randomization uses Local Admin MAC addresses. Ignoring Local
# Admin MAC addresses will cause false negatives. However, NOT ignoring
# Local Admin MAC addresses will cause false positives.
ADMIN_IGNORE = False

# (INT) RSSI threshold for triggering alerts
RSSI_THRESHOLD = -50

# (INT) Number of seconds between alerts for persistent foreign probes
ALERT_THRESHOLD = 120

# (STR) Path to the database file
LOG_FILE = 'log.db'

# (INT) Determines which probes are stored in the database
# 0 = all probes
# 1 = all foreign probes
# 2 = all probes on the premises
# 3 = all foreign probes on the premises
# 4 = only probes that generate alerts
LOG_LEVEL = 3

# (BOOL) Enable/Disable stdout debugging messages
DEBUG = False

#========
# ALERTS
#========

# (BOOL) Enable/Disable alert modules
#ALERT_SMS = True
#ALERT_PUSHOVER = True

#==================
# ALERT_SMS CONFIG
#==================

# (STR) SMTP server hostname and port (TLS required) for sending alerts
#SMTP_SERVER = 'smtp.gmail.com:587'

# (STR) Mail server credentials for sending alerts
#SMTP_USERNAME = ''
#SMTP_PASSWORD = ''

# (STR) SMS email address (through cellular service provider) for receiving alerts
#SMS_EMAIL = ''

#=======================
# ALERT_PUSHOVER CONFIG
#=======================

# (STR) API and User keys from pushover.net
#PUSHOVER_API_KEY = ''
#PUSHOVER_USER_KEY = ''
