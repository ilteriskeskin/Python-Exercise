import smtplib

host = "smtp.gmail.com"
port = 587
username = "mail_adresiniz@gmail.com"
password = "mail_parolanız"
from_email = username
to_list = ["selamet96@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Deneme1")
email_conn.quit()

from smtplib import SMTP

ABC = SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, "Deneme2")
ABC.quit()

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrong_password")
    pass_wrong.sendmail(from_email, to_list, "Deneme3")
except SMTPAuthenticationError:
    print('Could not login')
except:
    print('An error occured')

pass_wrong.quit()
