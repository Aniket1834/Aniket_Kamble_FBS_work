# Factorial

num = int(input("Enter a number : "))
fact = 1
if(num < 0):
    print("Factorial is not for negative number:")
    
elif(num == 0):
    print("factorial of 0 is 1")
    
else:
    for a in range(1,num+1):
        fact*=a
    print("Factorial of",num,"is",fact)