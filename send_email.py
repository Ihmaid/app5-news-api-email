import smtplib
import ssl
import os


def send_email(message):
    # Native configurations for Gmail
    host = "smtp.gmail.com"
    port = 465

    # This email is the sender of the message
    username = "teste1111python@gmail.com"
    # Environmental variable that refers to the app password
    password = os.getenv("PASSWORD")

    # This email is the receiver of the message
    receiver = "gabrielihm.ave@gmail.com"
    # Creation of a SSL context
    context = ssl.create_default_context()

    # Creation of a server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # The login with the email and the respective app password
        server.login(username, password)
        # Function to send the email
        server.sendmail(username, receiver, msg=message)
