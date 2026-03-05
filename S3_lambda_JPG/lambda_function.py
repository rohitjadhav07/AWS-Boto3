import json
import boto3
import os

s3 = boto3.client("s3")

ALLOWED_EXTENSIONS = (".jpeg", ".jpg", ".png")

def lambda_handler(event, context):
    try:
        for record in event["Records"]:
            bucket_name = record["s3"]["bucket"]["name"]
            file_key = record["s3"]["object"]["key"]

            print(f"Processing file: {file_key}")

            # Check extension
            if file_key.lower().endswith(ALLOWED_EXTENSIONS):
                print("File uploaded successfully (Valid format)")
            else:
                print("Invalid file format. Renaming file...")

                # Split filename
                file_name_without_ext = os.path.splitext(file_key)[0]
                new_file_key = file_name_without_ext + ".jpeg"

                # Copy object
                s3.copy_object(
                    Bucket=bucket_name,
                    CopySource={"Bucket": bucket_name, "Key": file_key},
                    Key=new_file_key
                )

                # Delete old object
                s3.delete_object(
                    Bucket=bucket_name,
                    Key=file_key
                )

                print(f"File renamed to: {new_file_key}")

        return {
            "statusCode": 200,
            "body": json.dumps("Processing completed")
        }

    except Exception as e:
        print("Error:", str(e))
        raise e