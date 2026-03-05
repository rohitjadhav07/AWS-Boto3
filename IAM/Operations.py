import boto3

iam = boto3.client('iam')

#-------------------------------------------------------------

#create user

# iam.create_user(UserName='rohit-user')
# print("User 'rohit-user' created successfully!")

#-------------------------------------------------------------

#create group

# iam.create_group(GroupName='rohit-group')
# print("Group 'rohit-group' created successfully!")

#-------------------------------------------------------------

#list groups
# response = iam.list_groups()

# for group in response['Groups']:
#     print(group['GroupName'])

#-------------------------------------------------------------

#add user to group
# iam.add_user_to_group(
#     GroupName='rohit-group',
#     UserName='rohit-user'
# )
# print("User 'rohit-user' added to group 'rohit-group' successfully!")

#-------------------------------------------------------------

#remove user from group

# iam.remove_user_from_group(
#     GroupName='rohit-group',
#     UserName='rohit-user'
# )
# print("User 'rohit-user' removed from group 'rohit-group' successfully!")

#-------------------------------------------------------------

#delete user

# iam.delete_user(UserName='rohit-user')
# print("User 'rohit-user' deleted successfully!")

#-------------------------------------------------------------

#delete group

# iam.delete_group(GroupName='rohit-group')
# print("Group 'rohit-group' deleted successfully!")

#-------------------------------------------------------------