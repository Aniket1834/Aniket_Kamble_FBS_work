#Swap Two Number Without Using third Variable

a = int(input("Enter First Num:"))
b = int(input("Enter Second Num:"))

# a = a + b 
# b = a - b 
# a = a - b 

a,b = b,a

print("a =",a)
print("b =",b)