from datetime import date

today = date.today()
print("Please enter the date you want to find out how many days until below: ")

try:
    year = int(input("What year? "))
    month = int(input("What month? "))
    day = int(input("What day? "))

    date2 = date(year, month, day)

    difference = date2 - today

    print(f"There are only {difference.days:,} days left until {date2} from {today}")

except ValueError:
    print("Please enter a correct value. ")