import email
import imaplib

# connect to the server and go to its inbox
server = imaplib.IMAP4_SSL('imap.gmail.com')  # port 993

# login
with open('password.txt', 'r') as f:
    password = f.read()
server.login("mail.testing0025@gmail.com", password)
server.select("INBOX")

# search using ALL criteria, get all unread messages
# (data is list of uids), use 'ALL' if want all emails
status, data = server.search(None, '(UNSEEN)')

# extract mail_ids
mail_ids = []
for block in data:
    mail_ids += block.split()  # b'1 2 3'.split() => [b'1', b'2', b'3']

# extract each email and contents
for i in mail_ids:
    # the fetch function fetch the email given its id and format
    status, data = server.fetch(i, '(RFC822)')

    # '(RFC822)' => a list with a tuple with header, content, and the closing byte b')'
    for response_part in data:
        # so if its a tuple...
        if isinstance(response_part, tuple):
            # use SECOND element (header is first and closing is last)
            message = email.message_from_bytes(response_part[1])

            mail_from = message['from']
            mail_subject = message['subject']

            # if not all plain text, seperate from annexes
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

            print(f'From: {mail_from}')
            print(f'Subject: {mail_subject}')
            print(f'Content: {mail_content}')