#Prime number n th time

start = int(input("Enter Start : "))
stop = int(input("Enter Stop : "))

for i in range(start,stop+1):
    if (i == 1):
            continue
        
    for j in range(2,i):
        
        
        
        if(i % j == 0):
            break
        
    else:
        print(i)
        