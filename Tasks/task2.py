import boto3
import time
import os
from botocore.exceptions import ClientError

# # ---------- CONFIG ----------
region = "ap-south-1"
bucket_name = "rohit-demo-bucket-1234569687"   # must be globally unique
file_name = "sample.txt"
object_name = file_name
expiration_time = 300   # 5 minutes in seconds

# # ---------- CREATE S3 CLIENT ----------
s3 = boto3.client("s3", region_name=region)

# # ---------- STEP 1: CREATE BUCKET ----------
# try:
#     s3.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={"LocationConstraint": region}
#     )
#     print("Bucket created successfully.")
# except ClientError as e:
#     print("Bucket creation error:", e)

# # ---------- STEP 2: CREATE TEXT FILE & UPLOAD ----------
# with open(file_name, "w") as f:
#     f.write("Hello Rohit! This is your S3 test file.")

# s3.upload_file(file_name, bucket_name, object_name)
# print("File uploaded successfully.")

# # ---------- STEP 3: LIST ALL OBJECTS ----------
# print("\nObjects inside bucket:")
# response = s3.list_objects_v2(Bucket=bucket_name)

# if "Contents" in response:
#     for obj in response["Contents"]:
#         print(" -", obj["Key"])
# else:
#     print("Bucket is empty.")

# # ---------- STEP 4: GENERATE PRE-SIGNED URL (VALID 5 MINUTES) ----------
# url = s3.generate_presigned_url(
#     "get_object",
#     Params={"Bucket": bucket_name, "Key": object_name},
#     ExpiresIn=expiration_time
# )

# print("\nShare this URL with your friend (valid 5 mins):")
# print(url)

# ---------- STEP 5: DOWNLOAD FILE & DELETE AFTER 5 MIN ----------
print("\nDownloading file...")
s3.download_file(bucket_name, object_name, "downloaded_" + file_name)
print("File downloaded.")

print("\nWaiting 5 minutes before deleting...")
time.sleep(expiration_time)

# Delete object
s3.delete_object(Bucket=bucket_name, Key=object_name)
print("Object deleted.")

# Optional: Delete bucket
s3.delete_bucket(Bucket=bucket_name)
print("Bucket deleted.")

# Clean local files
os.remove(file_name)
os.remove("downloaded_" + file_name)
print("Local files cleaned.")