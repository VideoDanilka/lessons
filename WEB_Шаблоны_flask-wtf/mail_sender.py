import smtplib
import mimetypes
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email, subject, text, attachments):
    addr_from = os.getenv('FROM')
    password = os.getenv("PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject

    body = text
    msg.attach(MIMEText(body, 'palin'))

    process_attachments(msg, attachments)

    server = smtplib.SMTP_SSL(os.getenv('HOST'), int(os.getenv('PORT')))
    server.login(addr_from, password)

    server.send_message(msg)
    server.quit()
    return True


def process_attachments(msg, attachments):
    pass
