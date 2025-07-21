#Average Marks of Students
n = int(input("Enter number of students: "))

avg_total = 0  # To store total of all percentages

for i in range(1, n + 1):
    print("\nEnter marks of student", i, ":")
    total = 0
    for j in range(1, 6):
        mark = int(input(f"  Subject {j} marks: "))
        total += mark
    
    perc = total / 5
    print("Percentage of student", i, ":", perc, "%")
    avg_total += perc

average = avg_total / n
print("\nAverage Percentage of all students:", average, "%")
