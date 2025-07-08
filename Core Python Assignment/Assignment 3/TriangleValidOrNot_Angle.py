# input angles of a triangle and check whether triangle is valid or not.

angle1 = int(input("Enter a first Angle:"))
angle2 = int(input("Enter a Secon Angle:"))
angle3 = int(input("Enter a Third Angle:"))

if(angle1+angle2+angle3==180):
    print("Triangle is Valid")
    
else:
    print("Triangle is Not Valid")