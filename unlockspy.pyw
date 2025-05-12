from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv
import os
import socket
import platform
import psutil
import uuid

def get_system_info():
    try:
        # Get IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        
        # Get system information
        system_info = {
            "OS": platform.system() + " " + platform.release(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Hostname": hostname,
            "IP": ip_address,
            "MAC": ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                            for elements in range(0,2*6,2)][::-1])
        }
        return system_info
    except Exception:
        return {"Hostname": socket.gethostname()}

# Load environment variables from .env
load_dotenv()

# Get credentials
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
TO_NUMBER = os.getenv("MY_WHATSAPP")
FROM_NUMBER = "[whatsapp:Twilio_whatsapp_number]"

# Get system information
sys_info = get_system_info()
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Enhanced message content
msg = f"""🔓 System Unlock Alert!

Time: {now}
Device: {sys_info['Hostname']}
OS: {sys_info['OS']}
IP: {sys_info['IP']}
MAC: {sys_info['MAC']}
Processor: {sys_info['Processor']}"""

try:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=msg,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
except Exception:
    pass  # Silent fail
