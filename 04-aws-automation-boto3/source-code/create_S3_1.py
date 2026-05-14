import boto3
import random

s3 = boto3.client("s3")

bucket_name = "rohit-project-bucket-" + str(random.randint(1000,9999))

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket Created:", bucket_name)