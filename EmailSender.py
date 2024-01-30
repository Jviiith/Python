
from email.message import EmailMessage
from password import app_password
import ssl
import smtplib


email_sender = 'jonathanokon98@gmail.com'
email_password = app_password

email_reciever = 'xilafa3773@evvgo.com'

subject = 'Python email test'
body = '''
Its Kishi here from your python program
'''
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
