# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas
import datetime as dt
import random
import smtplib
import os

now = dt.datetime.now()
today_day = now.day
today_month = now.month

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

letter_template_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthdays = pandas.read_csv("birthdays.csv")


for index in range(len(birthdays)):
    if today_day == birthdays.loc[index]["day"] and today_month == birthdays.loc[index]["month"]:

        name = birthdays.loc[index]["name"]
        letter_template = random.choice(letter_template_list)

        with open(f"./letter_templates/{letter_template}") as datafile:
            raw_letter = datafile.read()
            letter = raw_letter.replace("[NAME]", name)

        with smtplib.SMTP("mail.runbox.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthdays.loc[index]["email"],
                                msg=f"Subject: Happy Birthday!\n\n{letter}")
