from config import *

'''
Each module must receive **kwargs as a parameter. The kwargs variable is a dictionary
consisting of all the data extracted from the probe request. Each module name must
start with 'alert_' and have a matching variable in config.py for enabling/disabling.
Configurable module options may be defined in config.py.
'''

from email.mime.text import MIMEText
import smtplib

def alert_sms(**kwargs):
    msg = MIMEText('WUDS proximity alert! A foreign device (%s - %s) has been detected on the premises.' % (kwargs['bssid'], kwargs['oui']))
    server = smtplib.SMTP(SMTP_SERVER)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(SMTP_USERNAME, SMS_EMAIL, msg.as_string())
    server.quit()

import urllib
import urllib2

def alert_pushover(**kwargs):
    msg = 'Proximity alert! A foreign device (%s - %s) has been detected on the premises.' % (kwargs['bssid'], kwargs['oui'])
    url = 'https://api.pushover.net/1/messages.json'
    payload = {'token': PUSHOVER_API_KEY, 'user': PUSHOVER_USER_KEY, 'message': msg}
    payload = urllib.urlencode(payload)
    resp = urllib2.urlopen(url, data=payload)
