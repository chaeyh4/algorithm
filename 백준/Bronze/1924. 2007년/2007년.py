import datetime

x, y = map(int, input().split())

day = datetime.date(2007, x, y).weekday()

week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

print(week[day])