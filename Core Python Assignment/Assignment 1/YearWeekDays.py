#Find the year week and days in given days

days = int(input("Enter Days: "))
year = days//365
days = days % 365
weeks =days // 7
days = weeks % 7

print("Years",year,"Weeks",weeks,"Days",days)