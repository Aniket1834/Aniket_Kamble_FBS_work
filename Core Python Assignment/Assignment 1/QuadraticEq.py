# Quadratic Equation

a = int (input("Enter Number: "))
b = int (input("Enter Number: "))
c = int (input("Enter Number: "))

ans = (b*b) - (4*a*c)
ans = ans**0.5
root1=(-b +ans)/(2*a)
root2=(-b -ans)/(2*a)
print("Root 1:",root1)
print("Root 2:",root2)