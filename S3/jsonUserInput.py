import json
student=[]
count=int(input("How many students you want to enter: "))
for i in range(count):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))

    student.append({
        "name":name,
        "marks":marks
    })
with open("student.json","w") as f:
    json.dump(student,f) #dump to store in json file while writing 
topper =max(student,key=lambda x:x["marks"]) #lambda function is used to find the maximum marks in the list of students and return the student with the highest marks
print(topper)
