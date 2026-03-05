students={
    "rohit": 30,
    "sachin": 40,
    "virat": 50
}
name=input("enter the name of student: ")
if name in students:
    print("marks of",name,"are",students[name])
else:
    print("student not found")

for i in students:
    print(i,students[i])