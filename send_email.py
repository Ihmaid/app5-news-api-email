import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "teste1111python@gmail.com"
    # Environmental variable
    password = os.getenv("PASSWORD")

    receiver = "gabrielihm.ave@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg=message)
