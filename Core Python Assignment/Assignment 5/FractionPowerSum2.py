#x - x2/3 + x3/5 - x4/7 + …. to n terms
n = int(input("Enter n :"))
sum = 0

for a in range(1,n+1):
    sum+= (n ** a) / (n + 2)
    
print(sum)