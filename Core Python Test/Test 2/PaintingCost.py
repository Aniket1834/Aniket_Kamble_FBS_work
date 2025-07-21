height = float(input("Enter the height of wall (m): "))
width = float(input("Enter the width of wall (m): "))
cost_per_sq_meter = float(input("Enter painting cost per square meter: "))

area = 4 * height * width
total_cost = area * cost_per_sq_meter

print("Total painting cost = Rs.", round(total_cost, 2))
