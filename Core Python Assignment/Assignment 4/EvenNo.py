#Even or not

start = int(input("Enter a Start: "))
end = int(input("Enter a End: "))

for i in range(start,end+1):
    if(i % 2 == 0):
        print(i)
        