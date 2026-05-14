import boto3

elb = boto3.client("elbv2")

elb.create_listener(
    LoadBalancerArn="arn:aws:elasticloadbalancing:ap-south-1:362223162558:loadbalancer/app/MultiTierALB/5ad34ff3637fa3e9",
    Protocol="HTTP",
    Port=80,
    DefaultActions=[{
        "Type":"fixed-response",
        "FixedResponseConfig":{
            "StatusCode":"200",
            "ContentType":"text/plain",
            "MessageBody":"Multi-tier App Running"
        }
    }]
)

print("Listener Created")