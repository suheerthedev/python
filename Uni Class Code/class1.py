
totalMarks = [0,0,0]
stdName = ["","",""]
percentage = [0.0,0.0,0.0]
grade = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "C"]
grade.reverse()

for i in range(0,3):
    b = input("Enter Student Name:" )
    stdName[i] = b
    for j in range(0,3):
        a = int(input(f"Enter Marks of Course {j+1} Student {i+1}:  " ))
        totalMarks[i] += a
    percentage[i] = (totalMarks[i]/300)*100
    print(f"Percentage: {percentage[i]}")
    a = int(percentage[i]) / 10
    print(a)
    print(f"Grade: {grade[int(a)]}")