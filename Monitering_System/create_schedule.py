import boto3

scheduler = boto3.client("scheduler", region_name="ap-south-1")

response = scheduler.create_schedule(
    Name="system-health-schedule-boto3",
    ScheduleExpression="rate(1 minute)",
    FlexibleTimeWindow={"Mode": "OFF"},
    Target={
    "Arn": "arn:aws:lambda:ap-south-1:394901908305:function:system-health-monitor-boto3",
    "RoleArn": "arn:aws:iam::394901908305:role/scheduler-health-role"
}
)

print("Schedule created:", response["ScheduleArn"])