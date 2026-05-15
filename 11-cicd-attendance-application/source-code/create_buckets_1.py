import boto3
import random

s3 = boto3.client("s3", region_name="ap-south-1")

n = random.randint(1000,9999)

source = f"attendancecicdsource{n}"
deploy = f"attendancecicddeploy{n}"

for bucket in [source, deploy]:
    s3.create_bucket(
        Bucket=bucket,
        CreateBucketConfiguration={
            "LocationConstraint":"ap-south-1"
        }
    )

print("Source:", source)
print("Deploy:", deploy)