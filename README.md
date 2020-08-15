# mailing-client-python
Functions to automate sending emails and to deal with received emails. **Written to be used in another project that automates replies to certain emails.**

## Sending Emails
```sender.py``` can send emails. 
### To Use
For Gmail, you must either [allow less secure apps to access](https://myaccount.google.com/u/3/lesssecureapps) or [create an app password](https://support.google.com/accounts/answer/185833).

Use your email credentials in ```server.login("YOUR EMAIL", "YOUR PASSWORD")```. Update the last line for sending emails:  ```server.sendmail("YOUR EMAIL", "DESTINATION EMAIL", messageAsString)```.

### Implementation Notes
For Gmail (requires TLS), use code below (already in ```sender.py```):
```python
server = smtplib.SMTP("smtp.gmail.com", 587) # outgoing mail uses port 587
server.starttls()
```
*Read more [here](https://support.google.com/mail/answer/7126229?hl=en).*

Attachments need to be read as byte stream and encoded. See code for adding attachment under ```sender.py```.

## Receiving Emails
```receiver.py``` can get *all* or *unseen* emails and extract information.
### To use
For Gmail, first [enable IMAP](https://support.google.com/mail/answer/7126229?hl=en). 

Example output:
```html
From: "Mason Wang" <mason.wang0025@gmail.com>
Subject: Email Testing
Content: <html>
  <head></head>
  <body>
    <p>Hi!<br>
       HTML was extracted from this email. Plain text can also be extracted.
    </p>
  </body>
</html>
```
### Implementation Notes
```imaplib.error: command SEARCH illegal in state AUTH, only allowed in states SELECTED``` will be thrown if an inbox is not selected. ```server.select("INBOX")``` will suffice.

Payloads with multiple parts is handled with the following code:
```python
if message.is_multipart():
   mail_content = ''
   # if multipart, loop through payload
   for part in message.get_payload():
       # if the content type is text/plain we extract it
       if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
           mail_content += part.get_payload()
       else:
           # if the message isn't multipart, just extract it
           mail_content = message.get_payload()
```
