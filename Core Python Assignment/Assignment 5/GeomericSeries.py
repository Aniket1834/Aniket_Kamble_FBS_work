#Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter n: "))
sum_series = 0

for i in range(n): 
    geo = 2 ** i    
    sum_series += geo

print("Sum of Geometric series is", sum_series)
