#input all sides of a triangle and check whether triangle is valid or not

side1 = int(input("Enter First Side:"))
side2 = int(input("Enter a second Side:"))
side3 = int(input("Enter a Third Side:"))

if( side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    print("Triangle is valid")
    
else:
    print("Triangle is invalid")