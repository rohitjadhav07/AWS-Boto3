import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

s3.upload_file("test.txt", "rohit-image-trigger-bucket-12345", "test.txt")

print("File uploaded")