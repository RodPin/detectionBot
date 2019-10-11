import os
from twilio.rest import Client

account_sid = 'YOUR_TWILIO_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

from_whatsapp_number='whatsapp:+YOUR_TWILIO_POOL_NUMBER'
to_whatsapp_number='whatsapp:+YOUR_WHATSAPP_NUMBER'

msg='Movement detected'

message = client.messages.create(
from_=from_whatsapp_number,
body=msg,
to=to_whatsapp_number)
os.system('banner Done')
