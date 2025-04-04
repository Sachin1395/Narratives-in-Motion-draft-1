import smtplib


from Text_correction import generate

MY_EMAIL = "alansachin2010@gmail.com"
MY_PASSWORD = "lsjg blzg ypdq ontv"



def send_mail ( toadd, content):

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=toadd,
            msg=f"Subject: CONGRATS!! People has started liking your story, Here's your story branch suggestions\n\n{msg}"
        )





