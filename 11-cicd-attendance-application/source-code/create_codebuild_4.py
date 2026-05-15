import boto3

cb = boto3.client("codebuild")

cb.create_project(
 name="AttendanceBuild",
 serviceRole="arn:aws:iam::362223162558:role/AttendanceRole",
 artifacts={"type":"CODEPIPELINE"},
 environment={
   "type":"LINUX_CONTAINER",
   "image":"aws/codebuild/standard:7.0",
   "computeType":"BUILD_GENERAL1_SMALL",
   "privilegedMode":False
 },
 source={"type":"CODEPIPELINE"}
)

print("CodeBuild Created")