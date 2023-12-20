# Function to input grades for a given student
def input_grades(student_name):
    grades = []
    for i in range(1, 4):
        grade = int(input(f"Enter the grade {i} for {student_name}: "))
        grades.append({"name": f"math{i}", "grade": grade})
    return grades

# Input grades for each student
grade1s1, grade2s1, grade3s1 = input_grades("first")
grade1s2, grade2s2, grade3s2 = input_grades("second")

# Data
studentData = [
    {
        "student": "first",
        "lesson": [
            {"name": "math1", "grade": grade1s1},
            {"name": "math2", "grade": grade2s1},
            {"name": "math3", "grade": grade3s1}
        ]
    },
    {
        "student": "second",
        "lesson": [
            {"name": "math1", "grade": grade1s2},
            {"name": "math2", "grade": grade2s2},
            {"name": "math3", "grade": grade3s2}
        ]
    }
]

# First question: Print grades for each student
print("Your grades:")
for x in studentData:
    print(x["student"])
    for grade in x["lesson"]:
        print(grade["name"], ":", grade["grade"])

# Second question: Calculate and print the average grade for each student
print("\nYour average grades:")
for x in studentData:
    sum_num = sum(grade["grade"] for grade in x["lesson"])
    average = sum_num / len(x["lesson"])
    print(x["student"])
    print("Average Grade:", average)

# Third question: Print the minimum and maximum grades for each student
print("\nThe minimum and maximum grades:")
for x in studentData:
    min_num = min(grade["grade"] for grade in x["lesson"])
    max_num = max(grade["grade"] for grade in x["lesson"])
    print(x["student"])
    print("Minimum Grade:", min_num, "Maximum Grade:", max_num)
