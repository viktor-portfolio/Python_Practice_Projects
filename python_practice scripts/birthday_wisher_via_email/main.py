import pandas
import random
import smtplib
import datetime as dt

today = (dt.datetime.now().month, dt.datetime.now().day)

my_email = ""
my_password = ""
to_address_email = ""
signed = ""

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        letter = file.read()
        birthday_letter_name = letter.replace("[NAME]", birthday_dict[today]["name"])
        birthday_letter = birthday_letter_name.replace("[SIGNED]", signed)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_address_email,
                            msg=f"Subject:HAPPY BIRTHDAY\n\n{birthday_letter}"
                            )

