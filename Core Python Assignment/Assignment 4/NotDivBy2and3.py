#Not Divide By 2 and 3

start = int(input("Enter  start: "))
end = int(input("Enter end: "))

for i in range(start, end):
    if i % 2 != 0 and i % 3 != 0:
        print(i)
