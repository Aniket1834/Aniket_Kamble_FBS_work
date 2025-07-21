n = int(input("Enter number of employees : "))

for i in range(1,n+1):
    salary = int(input(f"Enter Basic Salary of employe {i} :"))
    if(salary>20000):
        da =salary * 0.15
        ta =salary * 0.18
        hra = salary * 0.20
        salary = salary + da +ta + hra
        
        print(f"Total salary of employee {i} is :{salary}" )
        
    elif(salary <= 20000):
        da =salary * 0.1
        ta =salary * 0.12
        hra = salary * 0.15
        salary = salary + da +ta + hra
        
        print(f"Total salary of Employee {i} is :{salary}" )
        
print("Done!!")