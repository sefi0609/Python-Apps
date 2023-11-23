import smtplib
import ssl
import os
import imghdr
from email.message import EmailMessage

host = 'smtp.gmail.com'
port = 465

username = 'sefi0609@gmail.com'

context = ssl.create_default_context()


def send_email(image):
    email_message = EmailMessage()
    email_message['Subject'] = 'Thief alert ! ! !'
    email_message.set_content('Hi, this guy just walk into your building')

    with open(image, 'rb') as f:
        content = f.read()

    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, os.getenv('Portfolio'))
        server.sendmail(username, username, email_message.as_string())
