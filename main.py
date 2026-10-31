import smtplib
import datetime as dt
import random

MY_EMAIL = "fahmiabdulaziz44@gmail.com"
MY_PASSWORD = "xxx"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as data_file:
        all_quotes = data_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}."
)
