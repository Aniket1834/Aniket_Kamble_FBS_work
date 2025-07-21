#1i to series

num = int(input("Enter range : "))
fact = 1
fact_sum = 0

for i in range (1, num+1):
    
    fact *=i
    fact_sum += fact
   
print("\nSum of factotial 1i to",num,"is :",fact_sum)    
    
