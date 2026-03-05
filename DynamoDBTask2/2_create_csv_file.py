import csv

data = [
    ["EmployeeID","Name","Department","Salary"],
    ["1","Rahul","Engineering","70000"],
    ["2","Amit","Finance","60000"],
    ["3","Neha","Engineering","72000"],
    ["4","Pooja","HR","50000"],
    ["5","Karan","Engineering","68000"]
]

with open("employees.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV file created")