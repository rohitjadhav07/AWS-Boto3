import boto3
import json
import time

iam = boto3.client("iam")

role_name = "lambda-polly-role"

assume_policy = {
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Principal": {"Service": "lambda.amazonaws.com"},
   "Action": "sts:AssumeRole"
  }
 ]
}

try:
    role = iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_policy)
    )
    print("Role created")
except iam.exceptions.EntityAlreadyExistsException:
    role = iam.get_role(RoleName=role_name)
    print("Role already exists")

role_arn = role["Role"]["Arn"]

policies = [
"arn:aws:iam::aws:policy/AmazonS3FullAccess",
"arn:aws:iam::aws:policy/AmazonPollyFullAccess",
"arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
]

for p in policies:
    iam.attach_role_policy(RoleName=role_name, PolicyArn=p)

print("Policies attached")

print("Waiting for role propagation...")
time.sleep(10)

print("Role ARN:", role_arn)