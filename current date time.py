from datetime import date,time,datetime

today = date.today()
print(today)

now = datetime.now()
print(now)

print(f"Current year: {today.year}")
print(f"Current Month: {today.month}")
print(f"Current day: {today.day}")
