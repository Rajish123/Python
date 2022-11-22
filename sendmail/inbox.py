# imap is a way to open your inbox
import imaplib
import email 

# imap host
host = 'imap.gmail.com'
username = "rajishmaharjan123@gmail.com"
password = "trdabcjnobmwvato"


def get_inbox_message():
    # login to imap mail server
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select("inbox")

    # search for unseen messages
    # _ is placeholder for a variable
    # if you want only one piece of data mainly in tuple 
    _, search_data = mail.search(None, "UNSEEN")

    my_message = []

    # split the data to iterate and find the messages thats related to 
    # split creates its own list
    for num in search_data[0].split():
        # creates a dictionary for the email message
        email_data = {}
        # each of this num references the email message that we are looking for
        # allow us to grab the correct message
        _, data = mail.fetch(num, '(RFC822)')
        _,b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject','to','from','date']:
            # print(f"{header}:{email_message[header]}")
            email_data[header] = email_message[header]
            
        # parsing data
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                # gives actual data thats in the content as bytes
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode() 
                
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox_message()
    print(my_inbox)
            