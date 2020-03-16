import smtplib
from email.encoders import encode_base64
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Gmail(object):
    def __init__(self, email, password):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        self.email = email
        self.password = password
        server.ehlo()
        server.starttls()
        server.login(self.email, self.password)
        self.server = server

    def send_message(self, to, subject, body):
        self.body = body
        self.subject = subject
        self.to = to
        from1 = self.email
        msg = MIMEText(body, 'plain', 'utf-8')
        msg["Subject"] = Header(subject, 'utf-8')
        msg["From"] = Header(from1, 'utf-8')
        msg["To"] = Header(to, 'utf-8')
        txt = msg.as_string()
        self.server.sendmail(from1, to, txt)

    def send_mail_attach(self, to, subject, body, filePath, newFileName, format):
        self.body = body
        self.subject = subject
        self.to = to
        self.filePath = filePath
        self.format = format
        from1 = self.email
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        msg["Subject"] = Header(subject, 'utf-8')
        msg["From"] = Header(from1, 'utf-8')
        msg["To"] = Header(to, 'utf-8')
        with open(filePath, "rb") as opened:
            openedfile = opened.read()
        attachedfile = MIMEApplication(openedfile, _subtype=format, _encoder=encode_base64)
        attachedfile.add_header('content-disposition', 'attachment', filename=newFileName)
        msg.attach(attachedfile)
        txt = msg.as_string()
        self.server.sendmail(from1, to, txt)

    def quit(self):
        self.server.quit()

