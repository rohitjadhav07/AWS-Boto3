import boto3

ec2 = boto3.client("ec2")

response = ec2.run_instances(
    ImageId="ami-0e12ffc2dd465f6e4",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="ProvisionKey"
)

print("EC2 Instance Created")
print(response["Instances"][0]["InstanceId"])