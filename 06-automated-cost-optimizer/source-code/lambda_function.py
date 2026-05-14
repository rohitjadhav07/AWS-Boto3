import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instances = ec2.describe_instances()

    stopped = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            tags = instance.get('Tags', [])

            for tag in tags:
                if tag['Key'] == 'AutoStop' and tag['Value'] == 'True':
                    if state == 'running':
                        ec2.stop_instances(InstanceIds=[instance_id])
                        stopped.append(instance_id)

    return {"Stopped": stopped}
