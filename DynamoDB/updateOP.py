import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

table = dynamodb.Table('Students')

# Scan the entire table
response = table.scan()

students = response['Items']

# Update marks
for student in students:
    
    table.update_item(
        Key={
            'StudentID': student['StudentID']
        },
        UpdateExpression="SET Marks = Marks + :inc",
        ExpressionAttributeValues={
            ':inc': 5
        }
    )

    print(f"Updated marks for StudentID {student['StudentID']}")

print("All students' marks increased by 5")