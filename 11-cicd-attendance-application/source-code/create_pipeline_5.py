import boto3

cp = boto3.client("codepipeline", region_name="ap-south-1")

pipeline = {
    "pipeline": {
        "name": "AttendancePipeline",
        "roleArn": "arn:aws:iam::362223162558:role/AttendanceRole",
        "artifactStore": {
            "type": "S3",
            "location": "attendancecicdsource3807"
        },
        "stages": [

            # -------------------------------
            # Source Stage
            # -------------------------------
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "Source",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "S3",
                            "version": "1"
                        },
                        "runOrder": 1,
                        "configuration": {
                            "S3Bucket": "attendancecicdsource3807",
                            "S3ObjectKey": "app.zip",
                            "PollForSourceChanges": "true"
                        },
                        "outputArtifacts": [
                            {"name": "SourceOutput"}
                        ],
                        "inputArtifacts": []
                    }
                ]
            },

            # -------------------------------
            # Build Stage
            # -------------------------------
            {
                "name": "Build",
                "actions": [
                    {
                        "name": "Build",
                        "actionTypeId": {
                            "category": "Build",
                            "owner": "AWS",
                            "provider": "CodeBuild",
                            "version": "1"
                        },
                        "runOrder": 1,
                        "configuration": {
                            "ProjectName": "AttendanceBuild"
                        },
                        "inputArtifacts": [
                            {"name": "SourceOutput"}
                        ],
                        "outputArtifacts": [
                            {"name": "BuildOutput"}
                        ]
                    }
                ]
            },

            # -------------------------------
            # Deploy Stage
            # -------------------------------
            {
                "name": "Deploy",
                "actions": [
                    {
                        "name": "Deploy",
                        "actionTypeId": {
                            "category": "Deploy",
                            "owner": "AWS",
                            "provider": "S3",
                            "version": "1"
                        },
                        "runOrder": 1,
                        "configuration": {
                            "BucketName": "attendancecicddeploy3807",
                            "Extract": "true"
                        },
                        "inputArtifacts": [
                            {"name": "BuildOutput"}
                        ]
                    }
                ]
            }

        ],
        "version": 1
    }
}

response = cp.create_pipeline(**pipeline)

print("Pipeline Created Successfully")
print("Pipeline Name: AttendancePipeline")