from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv
import os
import socket
import uuid

# Load environment variables from .env
load_dotenv()

# Get credentials
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
TO_NUMBER = os.getenv("MY_WHATSAPP")
FROM_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Gather system info
hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname(hostname)
except Exception:
    ip_address = "Unavailable"

# Get MAC address
mac_num = hex(uuid.getnode()).replace('0x', '').upper()
mac = ':'.join(mac_num[i:i+2] for i in range(0, 12, 2))

# Message content (professional, no emojis)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
msg = (
    f"System Unlock Notification\n"
    f"Time: {now}\n"
    f"Device Name: {hostname}\n"
    f"IP Address: {ip_address}\n"
    f"MAC Address: {mac}"
)

try:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=msg,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
except Exception as e:
    print(f"Error: {str(e)}")
    pass  # Silent fail
