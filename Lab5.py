#task 5.1
while True:
    try:
        speed = float(input("Enter the wind speed in miles per hour: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

conditions = [
    (1, "Calm"),
    (12, "Gentle breeze"),
    (30, "Strong breeze"),
    (46, "Gale"),
    (63, "Storm"),
    (74, "Violent storm"),
    (float('inf'), "Hurricane force")
]

for limit, condition in conditions:
    if speed < limit:
        print(condition)
        break

print("________________________________________________________________________")
#task 5.2
import re

while True:
    date = input("Please enter a date in the format dd/mm/yyyy: ")
    if re.match(r'\d{2}/\d{2}/\d{4}', date):
        break
    else:
        print("Invalid date format. Please enter in the format dd/mm/yyyy.")

day, month, year = date.split("/")
month = int(month)

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

month_name = month_names.get(month, "Invalid month")

print(f"{int(day)} {month_name} {year}")

print("________________________________________________________________________")
#task 5.3
while True:
    time = input("Please enter a time in the format hh:mm:ss: ")
    if re.match(r'\d{2}:\d{2}:\d{2}', time):
        break
    else:
        print("Invalid time format. Please enter in the format hh:mm:ss.")

hours, minutes, seconds = map(int, time.split(":"))

seconds += 1

if seconds == 60:
    seconds = 0
    minutes += 1

    if minutes == 60:
        minutes = 0
        hours += 1

        if hours == 24:
            hours = 0

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

print("________________________________________________________________________")
#challenge task 5.4
from datetime import datetime, timedelta

while True:
    date_str = input("Please enter a date in the format dd/mm/yyyy: ")
    if re.match(r'\d{2}/\d{2}/\d{4}', date_str):
        break
    else:
        print("Invalid date format. Please enter in the format dd/mm/yyyy.")

date = datetime.strptime(date_str, "%d/%m/%Y")

next_date = date + timedelta(days=1)

print(next_date.strftime("%d/%m/%Y"))

print("________________________________________________________________________")