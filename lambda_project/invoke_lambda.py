import boto3
import json

lambda_client = boto3.client("lambda", region_name="us-east-1")

response = lambda_client.invoke(
    FunctionName="hello-rohit-boto3",
    InvocationType="RequestResponse",
)

payload = json.loads(response["Payload"].read())

print("Lambda Response:")
print(payload)