#Convert the time entered in hh,min and sec into seconds
hour = int(input("Enter Hours: "))
minutes = int(input("Enter Minutes: "))
second = int(input("Enter second: "))

hour = hour*60*60
minutes = minutes*60

second = hour + minutes + second

print("Total Seconds",second)
