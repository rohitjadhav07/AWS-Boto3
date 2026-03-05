import boto3

lambda_client = boto3.client("lambda", region_name="ap-south-1")

with open("health_lambda.zip", "rb") as f:
    zipped_code = f.read()

response = lambda_client.create_function(
    FunctionName="system-health-monitor-boto3",
    Runtime="python3.9",
    Role="arn:aws:iam::394901908305:role/lambda-health-role-boto3",
    Handler="health_lambda.lambda_handler",
    Code={"ZipFile": zipped_code},
    Timeout=10,
    MemorySize=128,
    Publish=True
)

print("Lambda created successfully")