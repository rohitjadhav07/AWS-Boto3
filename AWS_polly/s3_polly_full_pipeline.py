import boto3
import uuid

region = "ap-south-1"

# Create clients
s3 = boto3.client("s3", region_name=region)
polly = boto3.client("polly", region_name=region)

# Create unique bucket name
bucket_name = f"polly-demo-{uuid.uuid4().hex[:8]}"

print("Creating bucket:", bucket_name)

# Create bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("Bucket created successfully")

# Create local text file
text_content = """
Hello Rohit.
This text file is stored in S3.
AWS Polly will convert this text into speech.
"""

file_name = "input.txt"

with open(file_name, "w") as f:
    f.write(text_content)

print("Local text file created")

# Upload file to S3
s3.upload_file(file_name, bucket_name, file_name)

print("File uploaded to S3")

# Read file from S3
response = s3.get_object(
    Bucket=bucket_name,
    Key=file_name
)

text = response["Body"].read().decode("utf-8")

print("\nText retrieved from S3:")
print(text)

# Convert to speech
speech = polly.synthesize_speech(
    Text=text,
    OutputFormat="mp3",
    VoiceId="Joanna",
    Engine="neural"
)

# Save audio
audio_file = "speech.mp3"

with open(audio_file, "wb") as f:
    f.write(speech["AudioStream"].read())

print("\nAudio generated:", audio_file)