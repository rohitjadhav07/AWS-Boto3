import boto3
import uuid
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ---------------- CONFIG ----------------
region = "ap-south-1"
image_path = "11.jpg"

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
print(f"\nNumber of faces detected: {len(faces)}")

# ---------------- DRAW BOUNDING BOXES ----------------

# Load image locally
image = Image.open(image_path)
img_width, img_height = image.size

fig, ax = plt.subplots(1)
ax.imshow(image)

for face in faces:
    box = face["BoundingBox"]

    # Convert normalized coordinates to pixels
    left = box["Left"] * img_width
    top = box["Top"] * img_height
    width = box["Width"] * img_width
    height = box["Height"] * img_height

    # Create rectangle
    rect = patches.Rectangle(
        (left, top),
        width,
        height,
        linewidth=2,
        edgecolor='red',
        facecolor='none'
    )

    ax.add_patch(rect)

plt.title(f"Faces Detected: {len(faces)}")
plt.axis('off')
plt.show()