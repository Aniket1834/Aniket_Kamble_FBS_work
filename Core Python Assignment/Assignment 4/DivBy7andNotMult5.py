#Divide by 7 but not multiple of 5

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start,end+1):
    if (i % 7==0 and i % 5!=0):
        print(i)