marks=[]
for i in range (5):
    m=int(input("Enter marks: "))
    marks.append(m)
    if m>=40:
        print("pass")
    else:
        print("fail")
total=sum(marks)
print(marks)
print("sum:",sum(marks))
print("Avg:",total/len(marks))