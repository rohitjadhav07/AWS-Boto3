import boto3

ec2 = boto3.client("ec2")

key = ec2.create_key_pair(KeyName="ProvisionKey")

with open("ProvisionKey.pem", "w") as f:
    f.write(key["KeyMaterial"])

print("Key Pair Created")