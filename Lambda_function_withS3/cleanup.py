import boto3

region = "ap-south-1"
bucket_name = "rohitj-trigger-bucket-12345"
function_name = "hello-rohit-s3-trigger212"

s3 = boto3.resource("s3", region_name=region)
lambda_client = boto3.client("lambda", region_name=region)

# 1️⃣ Delete all objects inside S3 bucket
print("Deleting all objects in bucket...")
bucket = s3.Bucket(bucket_name)
bucket.objects.all().delete()

# If versioning was enabled (safe check)
bucket.object_versions.all().delete()

print("All objects deleted.")

# 2️⃣ Delete the bucket
print("Deleting bucket...")
bucket.delete()
print("Bucket deleted.")

# 3️⃣ Delete Lambda function
print("Deleting Lambda function...")
lambda_client.delete_function(FunctionName=function_name)
print("Lambda deleted.")

print("✅ Cleanup Complete!")