#Reverse The Three Digit Number

num = int (input("Enter Number: "))

# a = num % 10
# num = num // 10
# c = num % 10
# b = num // 10

# reversenum = (a*100)+(b*10)+c
# print(reversenum)

a = num % 10
num = num // 10
b = num % 10 
reverse = (a*10)+b
c = num // 10
reverse = (reverse * 10)+c
print(reverse)