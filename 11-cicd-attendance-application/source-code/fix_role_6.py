import boto3
import json

iam = boto3.client("iam")

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "codepipeline.amazonaws.com",
                    "codebuild.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

iam.update_assume_role_policy(
    RoleName="AttendanceRole",
    PolicyDocument=json.dumps(trust_policy)
)

print("AttendanceRole trust policy updated successfully")