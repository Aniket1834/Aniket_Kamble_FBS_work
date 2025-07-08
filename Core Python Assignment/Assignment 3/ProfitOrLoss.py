# calculate profit or loss

Selling_Price = int(input("Enter a selling price:"))
Cost_Price = int(input("Enter Cost price:"))

if(Selling_Price > Cost_Price):
    Profit = Selling_Price - Cost_Price
    print("Profit Rs.",Profit)
    
elif(Cost_Price > Selling_Price):
    Loss = Cost_Price - Selling_Price
    print("Loss Rs.",Loss)
    
else:
    print("No Profit No Loss")