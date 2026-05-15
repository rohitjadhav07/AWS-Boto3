import boto3, json

iam = boto3.client("iam")

trust = {
 "Version":"2012-10-17",
 "Statement":[{
   "Effect":"Allow",
   "Principal":{"Service":"codebuild.amazonaws.com"},
   "Action":"sts:AssumeRole"
 }]
}

role = iam.create_role(
    RoleName="AttendanceRole",
    AssumeRolePolicyDocument=json.dumps(trust)
)

iam.attach_role_policy(
    RoleName="AttendanceRole",
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
)

print(role["Role"]["Arn"])