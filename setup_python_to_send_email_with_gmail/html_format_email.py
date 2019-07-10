from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "aliilteriskeskin@gmail.com"
password = "Msaia21322312."
from_email = username
to_list = ["selamet96@gmail.com"]

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg = MIMEMultipart("Alternative")
    the_msg['Subject'] = "Hello!"
    the_msg['From'] = from_email

    plain_text = "Deneme mesajı"
    html_text = """\
        <html>
            <head></head>
            <body>
                <p>Selam,<br>
                    Bu bir deneme <b>mesajı</b> <a href="ilteriskeskin.github.io">İlteriş Keskin</a>
                </p>
            </body>
        </html>
        """

    part_1 = MIMEText(plain_text, 'plain')
    part_2 = MIMEText(html_text, 'html')

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()

except smtplib.SMTPException:
    print('Error sending message')