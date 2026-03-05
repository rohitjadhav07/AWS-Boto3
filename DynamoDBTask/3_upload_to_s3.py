import boto3

region = "ap-south-1"
bucket_name = "university-students-bucket-demo-12345"

s3 = boto3.client("s3", region_name=region)

s3.upload_file("students.json", bucket_name, "students.json")

print("File uploaded to S3")