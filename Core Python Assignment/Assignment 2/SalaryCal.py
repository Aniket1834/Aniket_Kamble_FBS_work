#calculate total salary of employee

BasicSalary = int(input("Enter Basic Salary of Employee: "))

DA = (10/100)*BasicSalary
TA = (12/100)*BasicSalary
HRA = (15/100)*BasicSalary

TotalSalary = BasicSalary + DA + TA + HRA



print("Total Salary of Employee is: ",TotalSalary)
