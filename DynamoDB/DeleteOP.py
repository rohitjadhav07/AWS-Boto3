import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('Students')

# Scan the table
response = table.scan()
students = response['Items']

# Delete students with marks < 50
for student in students:
    
    if student['Marks'] < 50:
        
        table.delete_item(
            Key={
                'StudentID': student['StudentID']
            }
        )

        print(f"Deleted StudentID {student['StudentID']} with Marks {student['Marks']}")

print("\nDeletion completed")

# Scan again to get remaining students
response = table.scan()
remaining_students = response['Items']

# Print remaining students
print("\nRemaining Students")
print("--------------------------------------------------")
print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(
    "ID", "Name", "Age", "Subject", "Marks"))
print("--------------------------------------------------")

for student in remaining_students:
    print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(
        student['StudentID'],
        student['Name'],
        student['Age'],
        student['Subject'],
        student['Marks']
    ))