# This code snippet demonstrates how to create an EC2 instance using the Boto3 library in Python. Make sure to replace the `ImageId`, `InstanceType`, and other parameters with values that are appropriate for your AWS environment.

# import boto3

# ec2 = boto3.client('ec2', region_name='ap-south-1')

# response = ec2.run_instances(
#     ImageId='ami-019715e0d74f695be',  # Amazon Linux 2 (ap-south-1) – verify before using
#     InstanceType='t3.micro',         # Free tier eligible     # Replace with your keypair
#     MinCount=1,
#     MaxCount=1,         # Replace with your subnet
# )

# instance_id = response['Instances'][0]['InstanceId']
# print("EC2 Instance created:", instance_id)



#Checking status of the instance
# import boto3

# ec2 = boto3.client('ec2', region_name='ap-south-1')

# instance_id = "i-06e5cf32a9f9913c4"  # Replace with your instance ID

# response = ec2.describe_instances(InstanceIds=[instance_id])

# state = response['Reservations'][0]['Instances'][0]['State']['Name']

# print("Instance State:", state)



#stopping the instance

import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

instance_id = "i-061c537edf35e4a56"  # Replace with your instance ID

ec2.stop_instances(InstanceIds=[instance_id])

print("Stopping instance...")

ec2.terminate_instances(InstanceIds=[instance_id])

print("Terminating instance...")




# import boto3
# import os

# region = "ap-south-1"
# key_name = "rohit-simple-key"

# ec2 = boto3.client("ec2", region_name=region)

# # 1️⃣ Create Key Pair
# response = ec2.create_key_pair(KeyName=key_name)

# with open(f"{key_name}.pem", "w") as f:
#     f.write(response["KeyMaterial"])

# os.chmod(f"{key_name}.pem", 0o400)

# print("Key pair created.")

# # 2️⃣ Launch Instance (uses default VPC & default security group)
# instance = ec2.run_instances(
#     ImageId="ami-019715e0d74f695be",  # Verify in your region
#     InstanceType="t3.micro",
#     KeyName=key_name,
#     MinCount=1,
#     MaxCount=1
# )

# instance_id = instance["Instances"][0]["InstanceId"]

# print("Instance created:", instance_id)



