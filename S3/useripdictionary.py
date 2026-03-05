stu = {}
users=int(input("Enter the number of users: "))
for i in range(users):
    name=input("Enter the name of student: ")
    marks=int(input("Enter the marks of student: "))

    stu["name"] = name
    stu["marks"] = marks

    print(stu)

