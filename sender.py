import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# connect to server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# login
with open('password.txt', 'r') as f:
    password = f.read()

server.login("mail.testing0025@gmail.com", password)

# message
msg = MIMEMultipart()
msg['Subject'] = "Tester Email"
msg['From'] = "Mason's Email Client"
msg['To'] = "mason.wang0025@gmail.com"

# html message body
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       This email was sent with Python. Please see attached.<br>
       Here is a <a href="http://www.python.org">link</a>.
    </p>
  </body>
</html>
"""
msg.attach(MIMEText(html, 'html'))

# email attachment
attachment = open("attachment.pdf", "rb")
p = MIMEBase("application", "octet-stream") # payload object
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", "attachment; filename=attachment.pdf")
msg.attach(p)

# send mail
text = msg.as_string()
server.sendmail("mail.testing0025@gmail.com", "mason.wang0025@gmail.com", text)