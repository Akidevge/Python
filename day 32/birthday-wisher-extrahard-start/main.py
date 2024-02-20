##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import random
import smtplib
import pandas as pd
import datetime as dt
email = "sender@gmail.com"
app_password = "password"
receiver = "receiver@gmail.com"
Letterlist = ["day 32\\birthday-wisher-extrahard-start\\letter_templates\\letter_1.txt",
              "day 32\\birthday-wisher-extrahard-start\\letter_templates\\letter_2.txt",
              "day 32\\birthday-wisher-extrahard-start\\letter_templates\\letter_3.txt"]
today_date = dt.datetime.now()
month = today_date.month
day = today_date.day
df = pd.read_csv(r"day 32\birthday-wisher-extrahard-start\birthdays.csv")
Results = df.loc[(df["month"] == 2) & (df["day"] == 20)]
names = Results["name"].tolist()
for name in names:
    letter = random.choice(Letterlist)
    with open(f"day 32\\birthday-wisher-extrahard-start\\Output_letters\\{name}.txt", "w") as File:
        with open(f"{letter}", "r") as Sample:
            File.write(Sample.read())
    with open(f"day 32\\birthday-wisher-extrahard-start\\Output_letters\\{name}.txt", "r") as File:
        LetterContent = File.read()
        newLetter = LetterContent.replace("[NAME]", name)
    with open(f"day 32\\birthday-wisher-extrahard-start\\Output_letters\\{name}.txt", "w") as File:
        File.write(newLetter)
    with open(f"day 32\\birthday-wisher-extrahard-start\\Output_letters\\{name}.txt", "r") as File:
        LetterContent = File.read()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=app_password)
            connection.sendmail(from_addr=email,
                                to_addrs=receiver,
                                msg=f"Subject:Birthday Wishes\n\n{LetterContent}"
                                )
