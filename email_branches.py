import smtplib
MY_EMAIL = "alansachin2010@gmail.com"
MY_PASSWORD = "lsjg blzg ypdq ontv"
toadd = "sachin.a2023@vitstudent.ac.in"

def send_mail ( toadd, content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=toadd,
            msg=f"Subject: CONGRATS!! People has started liking your story, Here's your story branch suggestions\n\n{content}"
        )