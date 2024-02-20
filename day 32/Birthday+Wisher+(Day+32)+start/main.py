# ------------------------basic smtp mail code ----------------------#
# import smtplib
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=app_password)
#     connection.sendmail(from_addr=email,
#                         to_addrs=receiver,
#                         msg="Subject:SMTP email from Python app\n\nHey i just wanna say\n Either you run the day or the day runs you. - Jim Rohn"
#                         )
# ---------------------sending motivational email-------------------------#
import smtplib
import datetime as dt
import random
today = dt.datetime.now()
weekday = today.weekday()
weekday = 1
if weekday == 1:
    with open("day 32/Birthday+Wisher+(Day+32)+start/quotes.txt") as file:
        Allquote = file.readlines()
        quote = random.choice(Allquote)
        email = "xxxx@gmail.com"
        app_password = "xxxxxx"
        receiver = "xxxxxx@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=app_password)
            connection.sendmail(from_addr=email,
                                to_addrs=receiver,
                                msg=f"Subject:Monday Motivation\n\nHey i just wanna say\n {quote}"
                                )
