import boto3, json

iam = boto3.client("iam")

trust = {
 "Version":"2012-10-17",
 "Statement":[{
   "Effect":"Allow",
   "Principal":{"Service":[
       "codebuild.amazonaws.com",
       "codepipeline.amazonaws.com"
   ]},
   "Action":"sts:AssumeRole"
 }]
}

iam.create_role(
 RoleName="CICDRole",
 AssumeRolePolicyDocument=json.dumps(trust)
)

iam.attach_role_policy(
 RoleName="CICDRole",
 PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
)

print("Role Created")