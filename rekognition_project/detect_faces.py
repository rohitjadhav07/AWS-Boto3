import boto3
import uuid
import os

# ---------------- CONFIG ----------------
region = "ap-south-1"
image_path = "4. Pasport Size Photo.jpg"

bucket_name = f"rohit-rekognition-{uuid.uuid4().hex[:6]}"
object_name = os.path.basename(image_path)

# ---------------- CREATE CLIENTS ----------------
s3 = boto3.client("s3", region_name=region)
rekognition = boto3.client("rekognition", region_name=region)

# ---------------- CREATE BUCKET ----------------
print(f"Creating bucket: {bucket_name}")

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={"LocationConstraint": region}
)

# ---------------- UPLOAD IMAGE ----------------
print("Uploading image...")
s3.upload_file(image_path, bucket_name, object_name)

# ---------------- DETECT FACES ----------------
print("Detecting faces...")

response = rekognition.detect_faces(
    Image={
        "S3Object": {
            "Bucket": bucket_name,
            "Name": object_name
        }
    },
    Attributes=["DEFAULT"]
)

faces = response["FaceDetails"]

print("\n==============================")
print(f"Number of faces detected: {len(faces)}")
print("==============================")

for i, face in enumerate(faces, 1):
    print(f"Face {i} confidence: {face['Confidence']:.2f}%")
