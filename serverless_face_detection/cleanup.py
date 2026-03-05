import boto3
import json
from botocore.exceptions import ClientError

region = "ap-south-1"

bucket_name = "rohit-324-reck"
function_name = "serverlessFaceDetection"
role_name = "lambda-rekognition-role"

s3 = boto3.client("s3", region_name=region)
iam = boto3.client("iam")
lambda_client = boto3.client("lambda", region_name=region)

print("\nStarting cleanup...\n")

# ================= REMOVE S3 TRIGGER =================
print("Removing S3 notification configuration...")
try:
    s3.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration={}
    )
except Exception as e:
    print("S3 trigger removal error:", e)

# ================= DELETE S3 OBJECTS =================
print("Deleting all objects from bucket...")
s3_resource = boto3.resource("s3", region_name=region)
bucket = s3_resource.Bucket(bucket_name)

try:
    bucket.objects.all().delete()
except Exception as e:
    print("Object deletion error:", e)

# ================= DELETE S3 BUCKET =================
print("Deleting S3 bucket...")
try:
    bucket.delete()
except Exception as e:
    print("Bucket deletion error:", e)

# ================= REMOVE LAMBDA PERMISSIONS =================
print("Removing Lambda permissions...")
try:
    policy = lambda_client.get_policy(FunctionName=function_name)
    policy_doc = json.loads(policy["Policy"])

    for statement in policy_doc["Statement"]:
        lambda_client.remove_permission(
            FunctionName=function_name,
            StatementId=statement["Sid"]
        )
except lambda_client.exceptions.ResourceNotFoundException:
    pass
except Exception as e:
    print("Permission removal error:", e)

# ================= DELETE LAMBDA =================
print("Deleting Lambda function...")
try:
    lambda_client.delete_function(FunctionName=function_name)
except lambda_client.exceptions.ResourceNotFoundException:
    pass

# ================= DETACH IAM POLICIES =================
print("Detaching IAM policies...")

policies = [
    "arn:aws:iam::aws:policy/AmazonRekognitionFullAccess",
    "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
]

for policy in policies:
    try:
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy)
    except Exception:
        pass

# ================= DELETE IAM ROLE =================
print("Deleting IAM role...")
try:
    iam.delete_role(RoleName=role_name)
except iam.exceptions.NoSuchEntityException:
    pass

print("\n✅ CLEANUP COMPLETE")