import boto3

s3 = boto3.client("s3")

notification_configuration = {
    "LambdaFunctionConfigurations": [
        {
            "LambdaFunctionArn": "arn:aws:lambda:ap-south-1:394901908305:function:image-upload-checker",
            "Events": ["s3:ObjectCreated:*"]
        }
    ]
}

s3.put_bucket_notification_configuration(
    Bucket="rohit-image-trigger-bucket-12345",
    NotificationConfiguration=notification_configuration
)

print("Trigger added successfully")