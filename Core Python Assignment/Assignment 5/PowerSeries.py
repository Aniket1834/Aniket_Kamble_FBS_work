#N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent) 

n = int(input("Enter a n th Number :"))
sum = 0
for i in range(1,n+1):
   ans = n**i
   
   sum += ans
print("Sum of power of series 1 to",n,"is : ",sum)
   