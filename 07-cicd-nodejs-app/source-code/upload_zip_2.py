import boto3

s3 = boto3.client("s3")

bucket_name = "node-source-2718"

s3.upload_file("E:/AWS_Projects/Node_CI-CD_Pro7/Node_CI-CD_Pro7/app.zip", bucket_name, "app.zip")

print("ZIP Uploaded Successfully")