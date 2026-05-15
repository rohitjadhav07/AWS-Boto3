import boto3

s3 = boto3.client("s3")

bucket = "attendancecicdsource3807"

s3.upload_file("E:/AWS_Projects/Attendance_CICD_Pro11/Attendance_CICD_Pro11/app.zip", bucket, "app.zip")

print("Uploaded")