import boto3
import json

region = "ap-south-1"
bucket_name = "university-students-bucket-demo-12345"
file_key = "students.json"
table_name = "Students"

# AWS clients
s3 = boto3.client("s3", region_name=region)
dynamodb = boto3.resource("dynamodb", region_name=region)

table = dynamodb.Table(table_name)

# Read JSON file from S3
response = s3.get_object(Bucket=bucket_name, Key=file_key)

file_content = response["Body"].read().decode("utf-8")

data = json.loads(file_content)

students = data["students"]

inserted = 0
skipped = 0

# Insert only students with marks > 40
for student in students:

    if student["Marks"] > 40:

        table.put_item(Item=student)
        inserted += 1

        print(f"Inserted: {student['Name']} ({student['Marks']})")

    else:
        skipped += 1
        print(f"Skipped: {student['Name']} ({student['Marks']})")

print("\nSummary")
print("Inserted into DynamoDB:", inserted)
print("Skipped (Marks <= 40):", skipped)