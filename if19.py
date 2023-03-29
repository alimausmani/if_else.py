# 19. Write a python program to input basic salary of an employee 
# and calculate its Gross salary according to
# following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%



basic_salary=int(input("enter uor salary:"))
if basic_salary<=10000:
    HRA=basic_salary*20/100
    DA=basic_salary*80/100
    print(HRA)
    print(DA)
    print("Gross_salary=",basic_salary+HRA+DA)
elif 10000<=20000:
    HRA=basic_salary*25/100
    DA=basic_salary*90/100
    print("Gross_salary=",basic_salary+HRA+DA)
else:
    basic_salary>20000
    HRA=basic_salary*30/100
    DA=basic_salary*95/100
    print("Gross_salary=",basic_salary+HRA+DA)   