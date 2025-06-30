# code for sending SMS alert

from twilio.rest import Client
import os

# Twilio credentials (store securely in environment variables)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_auth_token")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "+1415xxxxxxx")  # Your Twilio number
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER", "+91xxxxxxxxxx")  # Receiver number

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms_alert(message="🚨 SafeVision Alert: Accident Detected"):
    """
    Send an SMS alert via Twilio.
    """
    try:
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=TARGET_PHONE_NUMBER
        )
        print(f" SMS sent. SID: {sms.sid}")
        return True
    except Exception as e:
        print(f" Failed to send SMS: {e}")
        return False
