import boto3

region = "ap-south-1"
bucket_name = "company-csv-lambda-bucket-12345"

s3 = boto3.client("s3", region_name=region)

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("Bucket created")