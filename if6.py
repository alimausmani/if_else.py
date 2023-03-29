# 6. Write a python program to check whether a year is leap year or not.

year=int(input("enter the year:"))
if year%4==0 or year%400==0 and year%100==0:
    print("it is a leap year")
else:
    print("it is not a leap year")    