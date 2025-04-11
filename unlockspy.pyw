from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv
import os
import socket

# Load environment variables from .env
load_dotenv()

# Get credentials
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
TO_NUMBER = os.getenv("MY_WHATSAPP")
FROM_NUMBER = "[whatsapp:Twilio_whatsapp_number]"

# Message content
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname()
msg = f"🔓 Device '{hostname}' was unlocked at {now}"

try:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=msg,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
except Exception:
    pass  # Silent fail
