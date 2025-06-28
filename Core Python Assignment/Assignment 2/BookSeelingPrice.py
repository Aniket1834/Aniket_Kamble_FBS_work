# calculate selling price of book

CostPrice = int(input("Enter Cost price of book: "))
discount = int(input("Enter Discount %: "))

DiscAmt = (discount*CostPrice)/100

SellingPrice = CostPrice - DiscAmt

print("Selling Price is: ",SellingPrice)