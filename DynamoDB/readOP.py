import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('Students')

# Ask user for StudentID
student_id = input("Enter Student ID: ")

# Fetch item from DynamoDB
response = table.get_item(
    Key={
        'StudentID': student_id
    }
)

# Check if student exists
if 'Item' in response:
    student = response['Item']

    print("\nStudent Details")
    print("------------------")
    print("ID:", student['StudentID'])
    print("Name:", student['Name'])
    print("Age:", student['Age'])
    print("Subject:", student['Subject'])
    print("Marks:", student['Marks'])

else:
    print("Student not found")