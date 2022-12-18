# **Problem 1: Create a function that takes two arguments: the original price
# and the discount percentage as integers and returns the final price after the discount.**
# **Problem 2: Create a function that takes the age in years and returns the age in days.**
# **Problem 3: Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.**
# **Bonus** *(Optional)*
# Create a function, get_days, that takes two dates and returns the number of days between the first and second date.
import math
from datetime import datetime as dt


def calcfinalprice(origPrice, discount):
    return origPrice - discount


def ageindays(ageinyrs):
    return ageinyrs * 365


def converttodegrees(rad):
    return math.cos(math.degrees(rad))


def get_days(date1, date2):
    return (dt.strptime(date1, "%Y/%m/%d") - dt.strptime(date2, "%Y/%m/%d")).days


def main():
    origPrice = float(input("Enter the original price:"))
    discount = float(input("Enter the discount:"))
    print("Final price :", calcfinalprice(origPrice, discount))
    ageinyrs = int(input("Enter age in years:"))
    print("Age in days :", ageindays(ageinyrs))
    rad = float(input("Enter a radian:"))
    print("Degrees :", converttodegrees(rad))
    date1 = input("Enter a date in yyyy/mm/dd format :")
    date2 = input("Enter a date in yyyy/mm/dd format :")
    print("Difference between dates: ", get_days(date1, date2))


main()
