#create a class of student and accept name and marks in the constructor 
#ask user how many studentds to enter, add name and marks in the list of students 
#convert list object to dictionary and add dictionary objects to list
#dump the list in json file
import json
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
student=[]
count=int(input("How many students you want to enter: "))
for i in range(count):
    name=input("Enter name: ")
    marks=int(input("Enter marks: ")) 
    s= Student(name,marks)
    student.append({"name": s.name,"marks":s.marks}) #__dict__ function can also be used to convert the object of class to dictionary
filename="student.json"    
with open(filename,"w") as json_file:
    json.dump(student,json_file) 
