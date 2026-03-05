import boto3
import uuid

region = "ap-south-1"

s3 = boto3.client("s3", region_name=region)

bucket_name = f"polly-pipeline-{uuid.uuid4().hex[:6]}"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("Bucket created:", bucket_name)

# Create folders
s3.put_object(Bucket=bucket_name, Key="input/")
s3.put_object(Bucket=bucket_name, Key="audio/")

print("Folders created: input/ and audio/")