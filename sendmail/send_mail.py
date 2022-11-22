import smtplib
from email.mime.text import MIMEText
# MIMEMultipart enables us to attach both plain text email and HTML email and files
from email.mime.multipart import MIMEMultipart

username = "username"
password = "password"


def send_mail(text = "Email Body", subject = 'Hello World', from_email = "TestUser <testuser3@gmail.com>", to_emails = [],html = None):
    # check if to_email is list or not.If yes throws error
    assert isinstance(to_emails, list)
    
    # you wont able to use string to send a valid email, for this you have to do default things 
    # that email have which can be done by importing few items
    msg = MIMEMultipart('alternative')
    msg["FROM"] = from_email
    msg['To'] = ",".join(to_emails)
    msg["Subject"] = subject
    
    txt_part = MIMEText(text,"plain")
    msg.attach(txt_part)
    
    if html!=None:
        html_part = MIMEText("<h1>This is working</h1>","html")
        msg.attach(html_part)
    
    msg_str = msg.as_string()
    
    # login to smtp server
    server = smtplib.SMTP(
        host = 'smtp.gmail.com',
        port = 587
    )
    server.ehlo() 
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
    
    # another way to login to smtp server
    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass 