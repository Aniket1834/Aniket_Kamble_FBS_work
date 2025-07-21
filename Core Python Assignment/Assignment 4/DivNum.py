#Numbers Divided by given number

start = int(input("Enter Start: "))
end = int(input("Enter End:"))
num = int(input("Enter a number"))
for i in range(start,end+1):
    if(i % num == 0):
        print(i)