import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('Students')

# Scan the table
response = table.scan()
students = response['Items']

print("\nStudents with Marks > 80")
for student in students:
    if student['Marks'] > 80:
        print(student['Name'], "-", student['Marks'])

students_sorted = sorted(students, key=lambda x: x['Marks'])

lowest = students_sorted[0]

highest = students_sorted[-1]

middle = students_sorted[len(students_sorted)//2]

print("\nHighest Marks Student")
print(highest['Name'], "-", highest['Marks'])

print("\nLowest Marks Student")
print(lowest['Name'], "-", lowest['Marks'])

print("\nMiddle Student")
print(middle['Name'], "-", middle['Marks'])