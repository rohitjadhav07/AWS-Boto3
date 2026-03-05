import boto3

region = "ap-south-1"

s3 = boto3.client("s3", region_name=region)
iam = boto3.client("iam")
lambda_client = boto3.client("lambda", region_name=region)

bucket_name = input("Enter bucket name to delete: ")
function_name = "polly_text_to_speech"
role_name = "lambda-polly-role"

print("\nStarting cleanup...\n")

# -----------------------------
# 1. Remove S3 trigger
# -----------------------------
try:
    s3.put_bucket_notification_configuration(
        Bucket=bucket_name,
        NotificationConfiguration={}
    )
    print("S3 trigger removed")
except Exception as e:
    print("S3 trigger removal skipped:", e)

# -----------------------------
# 2. Delete Lambda function
# -----------------------------
try:
    lambda_client.delete_function(FunctionName=function_name)
    print("Lambda function deleted")
except lambda_client.exceptions.ResourceNotFoundException:
    print("Lambda function not found")

# -----------------------------
# 3. Empty S3 bucket
# -----------------------------
try:
    response = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" in response:
        objects = [{"Key": obj["Key"]} for obj in response["Contents"]]

        s3.delete_objects(
            Bucket=bucket_name,
            Delete={"Objects": objects}
        )

        print("Bucket objects deleted")

except Exception as e:
    print("Error deleting objects:", e)

# -----------------------------
# 4. Delete bucket
# -----------------------------
try:
    s3.delete_bucket(Bucket=bucket_name)
    print("Bucket deleted")
except Exception as e:
    print("Bucket deletion failed:", e)

# -----------------------------
# 5. Detach IAM policies
# -----------------------------
policies = [
"arn:aws:iam::aws:policy/AmazonS3FullAccess",
"arn:aws:iam::aws:policy/AmazonPollyFullAccess",
"arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
]

for policy in policies:
    try:
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy)
        print("Policy detached:", policy.split("/")[-1])
    except Exception:
        pass

# -----------------------------
# 6. Delete IAM role
# -----------------------------
try:
    iam.delete_role(RoleName=role_name)
    print("IAM role deleted")
except iam.exceptions.NoSuchEntityException:
    print("IAM role not found")

print("\nCleanup complete")