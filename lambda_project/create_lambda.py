import boto3

lambda_client = boto3.client("lambda", region_name="us-east-1")

with open("lambda_function.zip", "rb") as f:
    zipped_code = f.read()

response = lambda_client.create_function(
    FunctionName="hello-rohit-boto3",
    Runtime="python3.9",
    Role="arn:aws:iam::394901908305:role/lambda-basic-execution-role",
    Handler="lambda_function.lambda_handler",
    Code=dict(ZipFile=zipped_code),
    Description="Simple Hello Rohit Lambda",
    Timeout=10,
    MemorySize=128,
    Publish=True,
)

print("Lambda Created Successfully!")
print(response["FunctionArn"])
