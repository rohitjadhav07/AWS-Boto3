import boto3
import time

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table_name = "Students"

# Create Table
table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'StudentID',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'StudentID',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Creating table...")
table.wait_until_exists()
print("Table created!")

# Insert Students
students = [
    {"StudentID":"1","Name":"Amit","Age":20,"Subject":"Math","Marks":35},
    {"StudentID":"2","Name":"Rahul","Age":21,"Subject":"Math","Marks":55},
    {"StudentID":"3","Name":"Sneha","Age":20,"Subject":"Math","Marks":42},
    {"StudentID":"4","Name":"Priya","Age":22,"Subject":"Math","Marks":38},
    {"StudentID":"5","Name":"Rohit","Age":21,"Subject":"Math","Marks":67},
    {"StudentID":"6","Name":"Neha","Age":20,"Subject":"Math","Marks":29},
    {"StudentID":"7","Name":"Karan","Age":23,"Subject":"Math","Marks":48},
    {"StudentID":"8","Name":"Pooja","Age":21,"Subject":"Math","Marks":73},
    {"StudentID":"9","Name":"Arjun","Age":22,"Subject":"Math","Marks":31},
    {"StudentID":"10","Name":"Anjali","Age":20,"Subject":"Math","Marks":50}
]

table = dynamodb.Table(table_name)

for student in students:
    table.put_item(Item=student)

print("Inserted 10 students")

# Scan and count marks > 40
response = table.scan()

count = 0

for item in response['Items']:
    if item['Marks'] > 40:
        count += 1

print("Students with marks > 40:", count)