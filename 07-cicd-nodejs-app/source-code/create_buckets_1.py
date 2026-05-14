import boto3
import random

s3 = boto3.client("s3")
region = "ap-south-1"

n = str(random.randint(1000,9999))

source_bucket = "node-source-" + n
deploy_bucket = "node-deploy-" + n

for bucket in [source_bucket, deploy_bucket]:
    s3.create_bucket(
        Bucket=bucket,
        CreateBucketConfiguration={
            "LocationConstraint": region
        }
    )
    print("Created:", bucket)

print("Save bucket names")