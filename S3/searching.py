name=input("Enter name you want to search: ")
found- False
with open ("names.txt","r") as f:
    for line in f:
        if line.strip()==name:
            print("found")
            found=True
            break
    if found==False:
        print("Not Found")