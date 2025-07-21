#Fibonacci series

num = int(input("Enter a num :"))

a1,a2=0,1
sum = 0
if (num<=0):
    print("Please enter a number greater than 0")

else:
    for i in range(0, num):
        print(sum,end=" ")
        a1 = a2
        a2 = sum
        sum = a1 + a2