import boto3
import json
import time

region = "ap-south-1"
account_id = "394901908305"
bucket_name = "rohitj-trigger-bucket-12345"
function_name = "hello-rohit-s3-trigger212"

s3 = boto3.client("s3", region_name=region)
lambda_client = boto3.client("lambda", region_name=region)

# 1️⃣ Create S3 bucket
print("Creating S3 bucket...")
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": region}
)

# 2️⃣ Read Lambda zip
with open("lambda_function.zip", "rb") as f:
    zipped_code = f.read()

# 3️⃣ Create Lambda function
print("Creating Lambda...")
response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime="python3.9",
    Role=f"arn:aws:iam::{account_id}:role/lambda-s3-role",
    Handler="lambda_function.lambda_handler",
    Code={"ZipFile": zipped_code},
    Timeout=10,
    MemorySize=128,
    Publish=True
)

# Wait until Lambda becomes active
print("Waiting for Lambda to become Active...")
while True:
    state = lambda_client.get_function_configuration(
        FunctionName=function_name
    )["State"]
    
    if state == "Active":
        break
    
    time.sleep(3)

print("Lambda Active!")

# 4️⃣ Add permission for S3 to invoke Lambda
lambda_client.add_permission(
    FunctionName=function_name,
    StatementId="s3invoke",
    Action="lambda:InvokeFunction",
    Principal="s3.amazonaws.com",
    SourceArn=f"arn:aws:s3:::{bucket_name}"
)

# 5️⃣ Configure S3 trigger
lambda_arn = f"arn:aws:lambda:{region}:{account_id}:function:{function_name}"

notification_config = {
    "LambdaFunctionConfigurations": [
        {
            "LambdaFunctionArn": lambda_arn,
            "Events": ["s3:ObjectCreated:*"]
        }
    ]
}

s3.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration=notification_config
)

print("✅ Deployment Complete!")