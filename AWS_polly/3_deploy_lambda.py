import boto3
import zipfile

region = "ap-south-1"

lambda_client = boto3.client("lambda", region_name=region)

function_name = "polly_text_to_speech"

lambda_code = '''
import boto3
import re
import urllib.parse

s3 = boto3.client("s3")
polly = boto3.client("polly")

def lambda_handler(event, context):

    print("Event:", event)

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    if not key.endswith(".txt"):
        return

    response = s3.get_object(Bucket=bucket, Key=key)
    text = response['Body'].read().decode("utf-8")

    paragraphs = [p.strip() for p in re.split(r'\\n\\s*\\n', text) if p.strip()]

    voices = ["Joanna","Matthew","Aditi"]

    for i, paragraph in enumerate(paragraphs):

        voice = voices[i % len(voices)]

        speech = polly.synthesize_speech(
            Text=paragraph,
            OutputFormat="mp3",
            VoiceId=voice,
            Engine="neural"
        )

        audio = speech["AudioStream"].read()

        key_out = f"audio/paragraph_{i+1}_{voice}.mp3"

        s3.put_object(
            Bucket=bucket,
            Key=key_out,
            Body=audio,
            ContentType="audio/mpeg"
        )

        print("Audio stored:", key_out)
'''

with open("lambda_function.py","w") as f:
    f.write(lambda_code)

with zipfile.ZipFile("lambda.zip","w") as z:
    z.write("lambda_function.py")

with open("lambda.zip","rb") as f:
    zipped_code = f.read()

role_arn = input("Paste Role ARN: ")

lambda_client.create_function(
FunctionName=function_name,
Runtime="python3.11",
Role=role_arn,
Handler="lambda_function.lambda_handler",
Code={"ZipFile": zipped_code},
Timeout=30,
MemorySize=256
)

print("Lambda deployed")