# Create bucket in s3, generate 25 text files dynamically, upload all 25 files to s3 bucket, use paginators to list all objects, for each object print file name, size and last modified time, count total no of objects uploaded  
# import boto3
# import os
# from datetime import datetime

# # -------- CONFIG --------
# region = "ap-south-1"
# bucket_name = "rohit-mini-challenge2121"  # Must be globally unique
# file_count = 25

# # -------- CREATE S3 RESOURCE --------
# s3 = boto3.resource("s3", region_name=region)
# client = boto3.client("s3", region_name=region)

# -------- 1️⃣ CREATE BUCKET --------
# # s3.create_bucket(
# #     Bucket=bucket_name,
# #     CreateBucketConfiguration={"LocationConstraint": region}
# # )

# # print("Bucket created successfully!")

# # -------- 2️⃣ GENERATE 25 TEXT FILES --------
# # for i in range(1, file_count + 1):
# #     file_name = f"file_{i}.txt"
# #     with open(file_name, "w") as f:
# #         f.write(f"This is dynamically generated file number {i}\n")
# #         f.write(f"Created at: {datetime.now()}\n")

# # print("25 files generated successfully!")

# # # -------- 3️⃣ UPLOAD FILES --------
# # bucket = s3.Bucket(bucket_name)

# # for i in range(1, file_count + 1):
# #     file_name = f"file_{i}.txt"
# #     bucket.upload_file(file_name, file_name)

# # print("All files uploaded successfully!")

# # -------- 4️⃣ USE PAGINATOR TO LIST OBJECTS --------
# paginator = client.get_paginator("list_objects_v2")
# pages = paginator.paginate(Bucket=bucket_name)

# total_objects = 0

# print("\nListing Uploaded Objects:\n")

# for page in pages:
#     if "Contents" in page:
#         for obj in page["Contents"]:
#             total_objects += 1
#             print(f"File Name: {obj['Key']}")
#             print(f"Size (bytes): {obj['Size']}")
#             print(f"Last Modified: {obj['LastModified']}")
#             print("-" * 40)

# # -------- 5️⃣ COUNT TOTAL OBJECTS --------
# print(f"\nTotal objects uploaded: {total_objects}")


import boto3

region = "ap-south-1"
bucket_name = "rohit-mini-challenge2121"  # Your bucket name

# Create S3 resource
s3 = boto3.resource("s3", region_name=region)

bucket = s3.Bucket(bucket_name)

# 1️⃣ Delete all objects inside bucket
bucket.objects.all().delete()

print("All objects deleted!")

# 2️⃣ Delete bucket
bucket.delete()

print("Bucket deleted successfully!")

