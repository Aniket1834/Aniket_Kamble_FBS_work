radius = 20
length = 50
breadth = 40
cost_per_meter = 35
pi = 3.14

semicircle = pi * radius
  
rectangle = length + 2 * breadth

total_fencing = (semicircle + rectangle) * 5

total_cost = total_fencing * cost_per_meter

print("Total cost of fencing = Rs.", round(total_cost, 2))
