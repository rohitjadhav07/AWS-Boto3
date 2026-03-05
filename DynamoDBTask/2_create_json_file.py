import json
import random

students = []

courses = ["AWS", "Python", "DevOps", "DataScience"]

# Generate 25 students
for i in range(1, 26):

    student = {
        "StudentID": str(i),
        "Name": f"Student{i}",
        "Age": random.randint(18, 23),
        "Course": random.choice(courses),
        "Marks": random.randint(20, 100)
    }

    students.append(student)

data = {"students": students}

# Save JSON file
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)

print("students.json created with 25 students")