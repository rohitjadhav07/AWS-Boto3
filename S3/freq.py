# sentence="The frequency of a word is the number of times it appears in a text."
# words=sentence.split()
# freq={
    
    
# }
# for p in words:
#     if p in freq:
#         freq[p] += 1
#     else:
#         freq[p] = 1

# print(freq)

#count of unique names given by user in set 
names=set()
n=int(input("Enter the number of names: ")) 
for i in range(n):
    name=input("Enter the name: ")
    names.add(name)
print("Unique names: ",names)

student.append(Student(name,marks).__dict__) #__dict__ is used to convert the object of class to dictionary
with open("student.json","w") as f:
    json.dump(student,f) #dump to store in json file while writing
