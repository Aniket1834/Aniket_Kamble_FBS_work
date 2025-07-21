#S = a + a2 / 2 + a3 / 3 + …… + a10 / 10 
n = 10
sum = 0
for i in range(1,n+1):
    sum += (n ** i)/i
    
print(sum)