# mailing-client-python
```sender.py``` can send emails. For Gmail, you must either [allow less secure apps to access](https://myaccount.google.com/u/3/lesssecureapps) or [create an app password](https://support.google.com/accounts/answer/185833).

For Gmail (requires TLS), use code below (already in ```sender.py```):
```python
server = smtplib.SMTP("smtp.gmail.com", 587) # outgoing mail uses port 587
server.starttls()
```
Read more [here](https://support.google.com/mail/answer/7126229?hl=en).
