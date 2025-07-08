# Check if a 3-digit Number is Palindrome

num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
else:
    print("Please enter a valid 3-digit number.")
