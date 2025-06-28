amount = int(input("Enter a Amount:"))

n500 = amount // 500
r_amount = amount % 500

n200 = r_amount // 200
r_amount = r_amount % 200

n100 = r_amount // 100
r_amount = r_amount % 100

n50 = r_amount // 50
r_amount = r_amount % 50

n20 = r_amount // 20
r_amount = r_amount % 20

n10 = r_amount // 10 
r_amount = r_amount % 10

c5 = r_amount // 5
r_amount = r_amount % 5

c2 = r_amount // 2
r_amount = r_amount % 2



print("500 :",n500,"notes")
print("200 :",n200,"notes")
print("100 :",n100,"notes")
print(" 50 :",n50,"notes")
print(" 20 :",n20,"notes")
print(" 10 :",n10,"notes")
print("  5 :",c5,"Coins")
print("  2 :",c2,"Coins")
print("  1 :",r_amount,"Coins")