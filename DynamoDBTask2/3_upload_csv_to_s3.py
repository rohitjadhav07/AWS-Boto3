import boto3

region = "ap-south-1"
bucket_name = "company-csv-data-bucket-12345"

s3 = boto3.client("s3", region_name=region)

s3.upload_file("employees.csv", bucket_name, "employees.csv")

print("CSV uploaded to S3")