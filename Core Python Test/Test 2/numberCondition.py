num = int(input("Enter a 3-digit number: "))

if num >= 100 and num <= 999:
    first = num // 100
    second = (num // 10) % 10
    third = num % 10

    if first == 2 * second and third == 2 * first:
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Not a 3-digit number")
