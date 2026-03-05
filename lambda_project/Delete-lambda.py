import boto3

lambda_client = boto3.client("lambda", region_name="us-east-1")

lambda_client.delete_function(FunctionName="hello-rohit-boto3")

print("Lambda Deleted")