#Calculate the days between two dates
from datetime import date

def calcNumOfDays(date1, date2):
    if date2 > date1:   
        return (date2-date1).days
    else:
        return (date1-date2).days

date1 = date(2025, 12, 17)
print("Date 1 entered :",date1)
date2 = date(2013, 2, 1)
print("Date 2 entered :",date2)
print("Number of days between two dates are ",calcNumOfDays(date1, date2), "days")