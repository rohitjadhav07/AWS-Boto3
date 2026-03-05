# import boto3
# from botocore.exceptions import ClientError

# region = "ap-south-1"
# bucket_name = "rohit-ec-sss"  # Must be globally unique

# s3 = boto3.client("s3", region_name=region) #s3 is the client object that allows us to interact with the S3 service. We specify the region where our bucket will be created or accessed.

# try:
#     # Create bucket
#     s3.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={"LocationConstraint": region}  
#     )
#     print("Bucket created successfully!")

# except ClientError as e:
#     print("Bucket creation issue:", e)
