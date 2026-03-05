import boto3

rekognition = boto3.client("rekognition")

def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            }
        },
        Attributes=["DEFAULT"]
    )

    face_count = len(response["FaceDetails"])

    print(f"Number of faces detected: {face_count}")

    return {
        "statusCode": 200,
        "body": f"Faces detected: {face_count}"
    }