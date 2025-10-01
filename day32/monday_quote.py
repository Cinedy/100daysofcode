#SMTP = Simple Mail Transfer Protocol
import datetime as dt
import smtplib
from random import choice

my_email = "siljecodes@gmail.com"
password = "ixsfcjrehpmflgsw"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", encoding="utf-8") as file:
        quote = file.readlines()
        random_quote = choice(quote)
        print(random_quote)

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Monday Quote \n\n{random_quote}"
                )
        print("Done")
    except Exception as e:
        print("Failed to send email")

else:
    print("Not today")