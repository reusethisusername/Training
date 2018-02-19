from datetime import datetime, date

date_of_birth = datetime.strptime(input("Enter date of birth in the format dd mm yyyy: "), "%d %m %Y")
future_day = datetime.strptime(
    input("Enter the date when you want to find the age, in the format dd mm yyyy: "), "%d %m %Y")


def calculate_age(sDate, eDate):
    #TODO: try except to compare dates
    return eDate.year - sDate.year - ((eDate.month, eDate.day) < (sDate.month, sDate.day))
    #TODO: calculate months as well

age = calculate_age(date_of_birth, future_day)
print(age)
