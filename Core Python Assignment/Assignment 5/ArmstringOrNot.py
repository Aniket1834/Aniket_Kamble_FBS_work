#Armstrong or not

num = int(input("|Enter a Number : "))
count = 0
temp = num

while (num!=0):
    a = num % 10
    num = num // 10
    count += 1
    
num = temp
sum = 0

while (num != 0):
    a = num % 10
    num = num // 10
    sum = sum+(a ** count)
    
if (sum == temp):
    print(temp,"is a Armstrong")
 
else:
    print(temp,"is not Armstrong")   