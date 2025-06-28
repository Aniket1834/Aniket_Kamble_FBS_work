#Compound interest

P = int(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = int (input("Enter Years: "))

A = P * (1 + R/100 )**T
CI = A - P

print("Compound Interest: ",CI)