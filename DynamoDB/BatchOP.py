import boto3
import random

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table_name = "Students50"

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
print("Table created")

table = dynamodb.Table(table_name)

# Batch write 50 students
with table.batch_writer() as batch:
    
    for i in range(1, 51):
        
        batch.put_item(
            Item={
                'StudentID': str(i),
                'Name': f'Student{i}',
                'Age': random.randint(18, 23),
                'Subject': 'Math',
                'Marks': random.randint(30, 100)
            }
        )

print("Inserted 50 students successfully")