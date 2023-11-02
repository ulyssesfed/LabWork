#task 5.1
speed = float(input("Enter the wind speed in miles per hour: "))

if speed < 1:
    print("Calm")
elif speed < 12:
    print("Gentle breeze")
elif speed < 30:
    print("Strong breeze")
elif speed < 46:
    print("Gale")
elif speed < 63:
    print("Storm")
elif speed < 74:
    print("Violent storm")
else:
    print("Hurricane force")

print("________________________________________________________________________")
#task 5.2
date = input("Please enter a date in the format dd/mm/yyyy: ")

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

month_name = month_names[month]

print(f"{int(day)} {month_name} {year}")

print("________________________________________________________________________")
#task 5.3

time = input("Please enter a time in the format hh:mm:ss: ")

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

date_str = input("Please enter a date in the format dd/mm/yyyy: ")

date = datetime.strptime(date_str, "%d/%m/%Y")

next_date = date + timedelta(days=1)

print(next_date.strftime("%d/%m/%Y"))

print("________________________________________________________________________")