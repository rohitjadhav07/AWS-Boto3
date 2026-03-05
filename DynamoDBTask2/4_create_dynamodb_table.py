import boto3

region = "ap-south-1"
table_name = "Employees"

dynamodb = boto3.resource("dynamodb", region_name=region)

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            "AttributeName": "EmployeeID",
            "KeyType": "HASH"
        }
    ],
    AttributeDefinitions=[
        {
            "AttributeName": "EmployeeID",
            "AttributeType": "S"
        }
    ],
    ProvisionedThroughput={
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5
    }
)

table.wait_until_exists()

print("DynamoDB Table Created")