# code to send email alert
import smtplib
from email.mime.text import MIMEText

def send_alert(msg="🚨 Accident Detected!"):
    sender_email = "" 
    receiver_email = ""
    app_password = ""  # Use Gmail app password here

    message = MIMEText(msg)
    message["Subject"] = "🚨 SafeVision Alert"
    message["From"] = sender_email
    message["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send alert: {e}")
