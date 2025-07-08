#Cost Of Painting 

Length = int(input("Enter Length of Wall (in meters): "))
breadth = int(input("Enter Breadth of Wall (in meters): "))


Cost_Interior = int(input("Enter Cost of Interior Colour Rs. per sq.m: "))
Cost_Exterior = int(input("Enter Cost of Exterior Colour Rs. per sq.m: "))

Area = Length * breadth

Interior_Walls = Area * 8  
Exterior_Walls = Area * 8  

Total_Interior_Area = Interior_Walls * 2
Total_Exterior_Area = Exterior_Walls * 2

Interior_Cost = Total_Interior_Area * Cost_Interior
Exterior_Cost = Total_Exterior_Area * Cost_Exterior
Total_Cost = Interior_Cost + Exterior_Cost


print("Total Interior Area:", Total_Interior_Area, "sq.m")
print("Total Exterior Area:", Total_Exterior_Area, "sq.m")
print("Cost of Interior Painting: Rs.", Interior_Cost)
print("Cost of Exterior Painting: Rs.", Exterior_Cost)
print("Total Cost for Painting Two Rooms: Rs.", Total_Cost)
