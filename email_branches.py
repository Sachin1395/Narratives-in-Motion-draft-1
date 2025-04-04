import smtplib
import unicodedata

from Text_correction import generate

MY_EMAIL = "alansachin2010@gmail.com"
MY_PASSWORD = "lsjg blzg ypdq ontv"

def unicode_to_ascii(text):
    return ''.join(
        c if ord(c) < 128 else unicodedata.normalize('NFKD', c).encode('ascii', 'ignore').decode('ascii')
        for c in text
    )

def send_mail ( toadd, content):
    msg =unicode_to_ascii(content)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=toadd,
            msg=f"Subject: CONGRATS!! People has started liking your story, Here's your story branch suggestions\n\n{msg}"
        )





