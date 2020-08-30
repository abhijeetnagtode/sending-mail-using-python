import smtplib
import os
from email.message import EmailMessage

''' for the crendential always use environment veriable to keep information safe'''
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'date at 6 pm'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ''              #just type reciver mail
msg.set_content('lets have a coffee at evening')


#to start the connectio
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
