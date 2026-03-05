import boto3

region="ap-south-1"

s3=boto3.client("s3",region_name=region)
lambda_client=boto3.client("lambda",region_name=region)
sts=boto3.client("sts")

bucket=input("Bucket name: ")
function_name="polly_text_to_speech"

account_id=sts.get_caller_identity()["Account"]

lambda_client.add_permission(
FunctionName=function_name,
StatementId="s3invoke",
Action="lambda:InvokeFunction",
Principal="s3.amazonaws.com",
SourceArn=f"arn:aws:s3:::{bucket}"
)

notification={
"LambdaFunctionConfigurations":[
{
"LambdaFunctionArn":f"arn:aws:lambda:{region}:{account_id}:function:{function_name}",
"Events":["s3:ObjectCreated:*"],
"Filter":{
"Key":{
"FilterRules":[
{"Name":"prefix","Value":"input/"},
{"Name":"suffix","Value":".txt"}
]
}
}
}
]
}

s3.put_bucket_notification_configuration(
Bucket=bucket,
NotificationConfiguration=notification
)

print("Trigger configured")

text="""Hello Rohit.
This is paragraph one.

This is paragraph two.

This is paragraph three.
"""

with open("test.txt","w") as f:
    f.write(text)

s3.upload_file("test.txt",bucket,"input/test.txt")

print("Test file uploaded")