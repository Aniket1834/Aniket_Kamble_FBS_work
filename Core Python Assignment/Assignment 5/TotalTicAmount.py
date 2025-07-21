#calculate total amount to ticket 

pase =int(input("Enter Number of passengers : "))
Ticket = int(input("Enter Ticket cost : "))
Total_Amount = 0

for i in range (1,pase+1):
    age =int(input("Enter age:"))
    
    if(age<=12):
        cost = Ticket * 0.7
    
    elif(age>= 59):
        cost = Ticket * 0.5
        
    else:
        cost = Ticket
        
    print("Ticket cost",i,"age",age,"Rs.",cost)
    
    Total_Amount += cost
    
print("Total cost of passengers :",Total_Amount)