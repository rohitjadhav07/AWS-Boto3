import boto3
import re

region = "ap-south-1"

# AWS clients
s3 = boto3.client("s3", region_name=region)
polly = boto3.client("polly", region_name=region)

# ---------------------------
# 1. Use existing bucket
# ---------------------------
bucket_name = "polly-demo-1b9d91"

print("Using existing bucket:", bucket_name)

# ---------------------------
# 2. Create local text file
# ---------------------------
text_content = """Hello Rohit.
This is the first paragraph of the AWS Polly demo.

This is the second paragraph.
It will be spoken using a different voice.

Finally this is the third paragraph.
This paragraph will use another voice.
"""

file_name = "input.txt"

with open(file_name, "w") as f:
    f.write(text_content)

# ---------------------------
# 3. Upload text file to S3
# ---------------------------
s3.upload_file(file_name, bucket_name, file_name)

print("Text file uploaded to S3\n")

# ---------------------------
# 4. Read text from S3
# ---------------------------
response = s3.get_object(
    Bucket=bucket_name,
    Key=file_name
)

text = response["Body"].read().decode("utf-8")

print("Text retrieved from S3:\n")
print(text)

# ---------------------------
# 5. Split into paragraphs
# ---------------------------
paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

print("\nParagraphs detected:", len(paragraphs))

# ---------------------------
# 6. Show available voices
# ---------------------------
voices_response = polly.describe_voices()

voice_list = []

print("\nAvailable Voices:\n")

for i, voice in enumerate(voices_response["Voices"]):
    print(f"{i+1}. {voice['Id']} ({voice['LanguageName']})")

    voice_list.append({
        "id": voice["Id"],
        "engine": voice["SupportedEngines"][0]
    })

# ---------------------------
# 7. User selects 3 voices
# ---------------------------
choices = input("\nSelect 3 voice numbers (comma separated): ")

selected_indexes = [int(x.strip())-1 for x in choices.split(",")]
selected_indexes = selected_indexes[:3]

print("\nGenerating audio files...\n")

# ---------------------------
# 8. Generate audio + upload to S3
# ---------------------------
for i, paragraph in enumerate(paragraphs):

    voice_id = voice_list[selected_indexes[i]]["id"]
    engine = voice_list[selected_indexes[i]]["engine"]

    response = polly.synthesize_speech(
        Text=paragraph,
        OutputFormat="mp3",
        VoiceId=voice_id,
        Engine=engine
    )

    audio_data = response["AudioStream"].read()

    output_file = f"paragraph_{i+1}_{voice_id}.mp3"

    # Save locally
    with open(output_file, "wb") as f:
        f.write(audio_data)

    # Upload to S3 audio folder
    s3.put_object(
        Bucket=bucket_name,
        Key=f"audio/{output_file}",
        Body=audio_data,
        ContentType="audio/mpeg"
    )

    print(f"Audio generated and uploaded: audio/{output_file}")

print("\nAll paragraphs converted and stored in S3 audio folder")