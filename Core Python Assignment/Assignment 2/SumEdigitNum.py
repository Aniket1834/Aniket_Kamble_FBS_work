num = int(input("Enter a Number: "))

a = num % 10               
b = num // 10              
c = b % 10                 
d = b // 10              

SumOfNum = a+c+d

print("Sum of the ",num," is :",SumOfNum)