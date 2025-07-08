#electricity unit charges and calculate total electricity bill 

units = float(input("Enter electricity units consumed: "))

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = (50 * 0.50) + (units - 50) * 0.75
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + (units - 150) * 1.20
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (units - 250) * 1.50

surcharge = bill * 0.20
total_bill = bill + surcharge

print("Total Electricity Bill (with 20% surcharge): Rs.", round(total_bill, 2))
