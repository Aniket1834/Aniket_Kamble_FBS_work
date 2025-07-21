#Odd Number

start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for a in range (start,end+1):
    if(a % 2 !=0):
        print(a)
    