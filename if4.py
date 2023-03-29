# 4. Write a python program to check whether a number is divisible by 5 and 11 or not.

num=int(input("enter the number:"))
if num%5==0 or num%11==0:
    print("it is divisible")
else:
    print("it is not divisible by 5 and 11")    