#SMTP = Simple Mail Transfer Protocol
from datetime import datetime
import pandas
import smtplib
import random

my_email = "siljecodes@gmail.com"
password = "ixsfcjrehpmflgsw"

today = datetime.now()
today_touple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_touple in birthdays_dict:
    birthday_person = birthdays_dict[today_touple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Happy Birthday! \n\n{contents}"
                )
            print("Done")
    except Exception as e:
        print("Failed to send email")

else:
    print("Not today")
