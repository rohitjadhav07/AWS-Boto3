# Creating andd uploading file to S3 bucket using boto3 library in Python

import boto3
from botocore.exceptions import ClientError

region = "ap-south-1"
bucket_name = "rohit-mini-challenge2121"  # Must be globally unique
file_path = "30 Questions.txt"

s3 = boto3.client("s3", region_name=region) #s3 is the client object that allows us to interact with the S3 service. We specify the region where our bucket will be created or accessed.

# try:
#     # Create bucket
#     s3.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={"LocationConstraint": region}  
#     )
#     print("Bucket created successfully!")

# except ClientError as e:
#     print("Bucket creation issue:", e)

# try:
#     # Upload file
#     s3.upload_file(file_path, bucket_name, "30 Questions.txt")
#     print("File uploaded successfully!")

# except ClientError as e:
#     print("Upload failed:", e)





#Downloading file from S3 bucket using boto3 library in Python

# import boto3
# from botocore.exceptions import ClientError

# region = "ap-south-1"
# bucket_name = "rohitfileupload21212"  # your bucket name
# s3_file_name = "30 Questions.txt"  # file name in S3
# local_file_name = "downloaded_example.txt"  # name to save locally

# # Create S3 client
# s3 = boto3.client("s3", region_name=region)

# try:
#     # Download file
#     s3.download_file(bucket_name, s3_file_name, local_file_name)
#     print("File downloaded successfully!")

# except ClientError as e:
#     print("Download failed:", e)




# Deleting file and bucket from S3 using boto3 library in Python

# import boto3
# from botocore.exceptions import ClientError

# region = "ap-south-1"
# bucket_name = "rohitfileupload21212"  # your bucket name
# file_name = "30 Questions.txt"  # file stored in S3

# s3 = boto3.client("s3", region_name=region)

# try:
#     # 1️⃣ Delete the file inside bucket
#     s3.delete_object(Bucket=bucket_name, Key=file_name)
#     print("File deleted successfully!")

# except ClientError as e:
#     print("Error deleting file:", e)

# try:
#     # 2️⃣ Delete the bucket
#     s3.delete_bucket(Bucket=bucket_name)
#     print("Bucket deleted successfully!")

# except ClientError as e:
#     print("Error deleting bucket:", e)





#Resource-based approach to upload file to S3 bucket using boto3 library in Python


# import boto3
# from botocore.exceptions import ClientError

# region = "ap-south-1"
# bucket_name = "rohitresourcebasedupload21212"  # Must be globally unique
# file_name = "30 Questions.txt"
# download_name = "downloaded_example_resource.txt"

# # Create S3 resource
# s3 = boto3.resource("s3", region_name=region)

# try:
#     # 1️⃣ Create bucket
#     s3.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={"LocationConstraint": region}
#     )
#     print("Bucket created successfully!")

# except ClientError as e:
#     print("Bucket creation error:", e)

# try:
#     # 2️⃣ Upload file
#     s3.Bucket(bucket_name).upload_file(file_name, file_name)
#     print("File uploaded successfully!")

# except ClientError as e:
#     print("Upload error:", e)

# try:
#     # 3️⃣ Download file
#     s3.Bucket(bucket_name).download_file(file_name, download_name)
#     print("File downloaded successfully!")

# except ClientError as e:
#     print("Download error:", e)

# try:
#     # 4️⃣ Delete file
#     s3.Object(bucket_name, file_name).delete()
#     print("File deleted successfully!")

#     # 5️⃣ Delete bucket
#     s3.Bucket(bucket_name).delete()
#     print("Bucket deleted successfully!")

# except ClientError as e:
#     print("Delete error:", e)
