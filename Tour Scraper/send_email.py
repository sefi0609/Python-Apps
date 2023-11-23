import smtplib
import ssl
import os


def send_email(extracted):
    """ Send an email with the new tour """
    host = 'smtp.gmail.com'
    username = 'sefi0609@gmail.com'
    port = 465

    context = ssl.create_default_context()

    message = 'Subject: New Tour is Coming Up' + '\n' + extracted

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, os.getenv('Portfolio'))
        server.sendmail(username, username, message)
