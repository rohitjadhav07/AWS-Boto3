import boto3

# Create S3 client
s3 = boto3.client('s3')

# Get bucket list
response = s3.list_buckets()

print("Your S3 Buckets:")

for bucket in response['Buckets']:
    print(bucket['Name'])
