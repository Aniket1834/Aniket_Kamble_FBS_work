# 5 subject marks from user and display grade

s1 = int(input("English: "))
s2 = int(input("Maths: "))
s3 = int(input("Science: "))
s4 = int(input("History: "))
s5 = int(input("Computer Science: "))

if (s1 > 100 or s2 > 100 or s3 > 100 or s4 > 100 or s5 > 100) or \
   (s1 < 0 or s2 < 0 or s3 < 0 or s4 < 0 or s5 < 0):
    print("Enter Valid Marks (0 to 100)")

elif (s1 < 35 or s2 < 35 or s3 < 35 or s4 < 35 or s5 < 35):
    print("Fail")

else:
    total_marks = s1 + s2 + s3 + s4 + s5
    per = total_marks / 5
    print("Percentage:", per)

    if per >= 80:
        print("Distinction")
    elif per >= 70:
        print("First class")
    elif per >= 50:
        print("Second class")
    elif per >= 35:
        print("Pass")
