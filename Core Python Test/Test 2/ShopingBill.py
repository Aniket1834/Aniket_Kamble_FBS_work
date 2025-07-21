p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

total = p1 + p2 + p3 + p4 + p5
gst = total * 0.18
final = total + gst

print("Total bill with 18% GST = Rs.", round(final, 2))
