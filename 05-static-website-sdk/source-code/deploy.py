import boto3
import os
import json

# CONFIG
bucket_name = "my-static-site-unique-450"   # change if bucket already exists
region = "ap-south-1"
website_folder = "E:/AWS_Projects/AutomateStaticWebHosting_5/static-site"

s3 = boto3.client('s3', region_name=region)

# 1️⃣ Create bucket
print("Creating bucket...")
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
except Exception as e:
    print("Bucket may already exist:", e)

# 2️⃣ Disable block public access
print("Disabling block public access...")
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

# 3️⃣ Add bucket policy (FIXED ✅)
print("Adding bucket policy...")

policy_dict = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
        }
    ]
}

policy = json.dumps(policy_dict)

s3.put_bucket_policy(Bucket=bucket_name, Policy=policy)

# 4️⃣ Enable static website hosting
print("Enabling static hosting...")
s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        'IndexDocument': {'Suffix': 'index.html'},
        'ErrorDocument': {'Key': 'error.html'}
    }
)

# 5️⃣ Upload files
print("Uploading files...")

files = os.listdir(website_folder)
print("Files found:", files)

for file in files:
    file_path = os.path.join(website_folder, file)

    print("Uploading:", file)

    s3.upload_file(
        file_path,
        bucket_name,
        file,
        ExtraArgs={'ContentType': 'text/html'}
    )

print("✅ Website deployed successfully!")

# 6️⃣ Print website URL
print(f"🌐 Website URL: http://{bucket_name}.s3-website-{region}.amazonaws.com")