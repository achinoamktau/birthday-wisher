import pandas
import os
import random
import smtplib
import datetime as dt

my_email = "your_mail"
password = "your_own"


def send_mail(receiver):
    num = random.randint(1, 3)
    if num == 1:
        file = open("letter_templates/letter_1.txt")
    elif num == 2:
        file = open("letter_templates/letter_2.txt")
    else:
        file = open("letter_templates/letter_2.txt")
    name = receiver["name"]
    letter = file.read()
    file.close()
    letter = letter.replace("[NAME]", name)
    rec_email = receiver["email"]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=rec_email, msg=f"Subject: Happy Birthday\n\n{letter}")


day = dt.datetime.now().day
month = dt.datetime.now().month

df = pandas.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

for person in birthdays:
    if person["month"] == month and person["day"] == day:
        send_mail(person)




