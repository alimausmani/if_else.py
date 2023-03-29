# 13. Write a python program to count the total number of notes in a given amount.

amount=int(input("enter the amount:"))
if amount>=2000:
    a=amount//2000
    print("2000",a) 
amount=amount%2000
if amount<2000:
    b=amount//500
    print("500",b) 
amount=amount%500
if amount<500:
    c=amount//200
    print("200",b)
amount=amount%200
if amount<200:
    d=amount//100
    print("100",d)
amount=amount%100
if amount<100:
    e=amount//50
    print("50",e)
amount=amount%50
if amount<50:
    f=amount//20
    print("20",f)
amount=amount%20
if amount<20:
    g=amount//10
    print("10",g)
amount=amount%10
if amount<10:
    h=amount//5
    print("5",h) 
amount=amount%5
if amount<5:
    i=amount//2
    print("5",i)
amount=amount%2 
if amount<2:
    j=amount//1
    print("2",j)
amount=amount%1
if amount<1:
    print("1",amount)
print("notes",a+b+c+d+e+f+g+h+i+j+amount)                  
