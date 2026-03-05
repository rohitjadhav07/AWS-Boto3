import boto3

s3 = boto3.client("s3")

bucket = "polly-pipeline-a74dcd"

text = """Hello Rohit.
This is paragraph one.

This is paragraph two.

This is paragraph three.
"""

with open("test.txt","w") as f:
    f.write(text)

s3.upload_file("test.txt", bucket, "input/test.txt")

print("File uploaded")