# Total Ticket Amount with Age-Based Discount

total_amount = 0

age1 = int(input("Enter age of person 1: "))
price1 = float(input("Enter ticket price for person 1: "))
if age1 < 12:
    price1 *= 0.70  # 30% discount
elif age1 > 59:
    price1 *= 0.50  # 50% discount
total_amount += price1

age2 = int(input("Enter age of person 2: "))
price2 = float(input("Enter ticket price for person 2: "))
if age2 < 12:
    price2 *= 0.70
elif age2 > 59:
    price2 *= 0.50
total_amount += price2

age3 = int(input("Enter age of person 3: "))
price3 = float(input("Enter ticket price for person 3: "))
if age3 < 12:
    price3 *= 0.70
elif age3 > 59:
    price3 *= 0.50
total_amount += price3

age4 = int(input("Enter age of person 4: "))
price4 = float(input("Enter ticket price for person 4: "))
if age4 < 12:
    price4 *= 0.70
elif age4 > 59:
    price4 *= 0.50
total_amount += price4

age5 = int(input("Enter age of person 5: "))
price5 = float(input("Enter ticket price for person 5: "))
if age5 < 12:
    price5 *= 0.70
elif age5 > 59:
    price5 *= 0.50
total_amount += price5

print("Total ticket amount to be paid for 5 persons is:", total_amount)
