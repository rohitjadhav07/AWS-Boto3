import boto3

cb = boto3.client("codebuild")

cb.create_project(
    name="NodeBuild",
    source={"type":"CODEPIPELINE"},
    artifacts={"type":"CODEPIPELINE"},
    environment={
        "type":"LINUX_CONTAINER",
        "image":"aws/codebuild/standard:7.0",
        "computeType":"BUILD_GENERAL1_SMALL",
        "privilegedMode":False
    },
    serviceRole="arn:aws:iam::362223162558:role/CICDRole"
)

print("CodeBuild Created")