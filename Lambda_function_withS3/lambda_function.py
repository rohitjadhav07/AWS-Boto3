import json

def lambda_handler(event, context):
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(f"File uploaded: {file_name}")
    print(f"Bucket: {bucket_name}")

    return {
        "statusCode": 200,
        "body": json.dumps(f"{file_name} uploaded successfully!")
    }