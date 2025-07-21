n = int(input("Enter n th Number : "))

fact =1
sum = 0
for i in range (1,n+1):
    fact*=i
    a=i/fact
    sum+=a
    
print(sum)