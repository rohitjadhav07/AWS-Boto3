import boto3
import csv
import io

region = "ap-south-1"
bucket_name = "company-csv-data-bucket-12345"
file_key = "employees.csv"
table_name = "Employees"

s3 = boto3.client("s3", region_name=region)
dynamodb = boto3.resource("dynamodb", region_name=region)

table = dynamodb.Table(table_name)

response = s3.get_object(Bucket=bucket_name, Key=file_key)

content = response["Body"].read().decode("utf-8")

csv_reader = csv.DictReader(io.StringIO(content))

for row in csv_reader:

    table.put_item(
        Item={
            "EmployeeID": row["EmployeeID"],
            "Name": row["Name"],
            "Department": row["Department"],
            "Salary": int(row["Salary"])
        }
    )

    print("Inserted:", row["Name"])

print("All records inserted into DynamoDB")