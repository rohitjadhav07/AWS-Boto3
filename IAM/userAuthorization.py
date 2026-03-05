import boto3

iam = boto3.client('iam')

# username = "rohit-ec2-user"

# # 1️⃣ Create IAM User
# iam.create_user(UserName=username)
# print("User created.")

# # 2️⃣ Create Console Login Password
# iam.create_login_profile(
#     UserName=username,
#     Password="Rohit@12345",   # Must follow password policy
#     PasswordResetRequired=True
# )
# print("Console login enabled.")

# # 3️⃣ Create Access Key (Programmatic access)
# access_key = iam.create_access_key(UserName=username)

# print("Access Key ID:", access_key['AccessKey']['AccessKeyId'])
# print("Secret Access Key:", access_key['AccessKey']['SecretAccessKey'])

# # 4️⃣ Attach EC2 Full Access Policy
# iam.attach_user_policy(
#     UserName=username,
#     PolicyArn="arn:aws:iam::aws:policy/AmazonEC2FullAccess"
# )

# print("EC2 access granted.")


iam.delete_user(UserName='rohit-ec2-user')
print("User 'rohit-ec2-user' deleted successfully!")