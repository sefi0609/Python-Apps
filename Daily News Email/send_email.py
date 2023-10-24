import os
import smtplib
import ssl


def send_email(message):
    username = 'sefi0609@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(username, os.getenv('Portfolio'))
        server.sendmail(username, username, message)
