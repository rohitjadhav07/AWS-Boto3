import boto3
import json
import zipfile
import time
from botocore.exceptions import ClientError

region = "ap-south-1"

bucket_name = "rohit-324-reck"
role_name = "lambda-rekognition-role"
function_name = "serverlessFaceDetection"

s3 = boto3.client("s3", region_name=region)
iam = boto3.client("iam")
lambda_client = boto3.client("lambda", region_name=region)
sts = boto3.client("sts")

account_id = sts.get_caller_identity()["Account"]

# ================= S3 BUCKET =================
print("\nChecking/Creating S3 bucket...")

try:
    s3.head_bucket(Bucket=bucket_name)
    print("Bucket already exists.")
except ClientError:
    print("Creating bucket...")
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": region}
    )

# ================= IAM ROLE =================
print("\nChecking/Creating IAM role...")

assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}

try:
    iam.get_role(RoleName=role_name)
    print("IAM role already exists.")
except iam.exceptions.NoSuchEntityException:
    print("Creating IAM role...")
    iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )

    policies = [
        "arn:aws:iam::aws:policy/AmazonRekognitionFullAccess",
        "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    ]

    for policy in policies:
        iam.attach_role_policy(RoleName=role_name, PolicyArn=policy)

    print("Waiting for IAM propagation...")
    time.sleep(15)

role_arn = iam.get_role(RoleName=role_name)["Role"]["Arn"]

# ================= PACKAGE LAMBDA =================
print("\nPackaging Lambda code...")

with zipfile.ZipFile("lambda.zip", "w") as z:
    z.write("lambda_function.py")

# ================= CREATE OR UPDATE LAMBDA =================
print("\nChecking/Creating Lambda function...")

try:
    lambda_client.get_function(FunctionName=function_name)
    print("Lambda exists — updating code...")
    lambda_client.update_function_code(
        FunctionName=function_name,
        ZipFile=open("lambda.zip", "rb").read()
    )
    lambda_arn = lambda_client.get_function(
        FunctionName=function_name
    )["Configuration"]["FunctionArn"]
except lambda_client.exceptions.ResourceNotFoundException:
    print("Creating Lambda...")
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime="python3.9",
        Role=role_arn,
        Handler="lambda_function.lambda_handler",
        Code={"ZipFile": open("lambda.zip", "rb").read()},
        Timeout=10,
        MemorySize=128,
        Publish=True
    )
    lambda_arn = response["FunctionArn"]

print("Waiting for Lambda readiness...")
time.sleep(10)

# ================= CLEAN OLD PERMISSIONS =================
print("\nCleaning old Lambda permissions...")

try:
    policy = lambda_client.get_policy(FunctionName=function_name)
    policy_doc = json.loads(policy["Policy"])

    for statement in policy_doc["Statement"]:
        if statement["Principal"].get("Service") == "s3.amazonaws.com":
            lambda_client.remove_permission(
                FunctionName=function_name,
                StatementId=statement["Sid"]
            )
except lambda_client.exceptions.ResourceNotFoundException:
    pass

# ================= ADD NEW PERMISSION =================
print("Adding fresh S3 invoke permission...")

statement_id = f"s3invoke-{bucket_name}"

lambda_client.add_permission(
    FunctionName=function_name,
    StatementId=statement_id,
    Action="lambda:InvokeFunction",
    Principal="s3.amazonaws.com",
    SourceArn=f"arn:aws:s3:::{bucket_name}",
    SourceAccount=account_id
)

time.sleep(10)

# ================= CONFIGURE S3 TRIGGER =================
print("\nConfiguring S3 trigger...")

notification_configuration = {
    "LambdaFunctionConfigurations": [
        {
            "LambdaFunctionArn": lambda_arn,
            "Events": ["s3:ObjectCreated:*"]
        }
    ]
}

s3.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration=notification_configuration
)

print("\n✅ DEPLOYMENT SUCCESSFUL")
print(f"Bucket: {bucket_name}")
print(f"Lambda: {function_name}")