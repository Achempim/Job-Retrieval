import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    sender = "your-email@gmail.com"
    recipient = "emailme@email.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender, 'your-password')
        server.sendmail(sender, recipient, msg.as_string())

send_email("Top Job Alerts", "Check out the latest jobs on your dashboard!")
