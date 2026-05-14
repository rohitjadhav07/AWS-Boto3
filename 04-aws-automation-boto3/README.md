# Automate AWS Resource Provisioning using boto3

## 📌 Project Overview
This project demonstrates how to automate AWS infrastructure provisioning using Python boto3 scripts instead of manually creating resources from the AWS Management Console.

The project automates the creation of AWS resources including EC2 instances, Security Groups, S3 buckets, and EC2 Key Pairs.

---

## 🎯 Objective
- Automate AWS resource provisioning
- Create infrastructure using Python scripts
- Generate EC2 Key Pairs programmatically
- Reduce manual AWS Console operations

---

## 🧰 AWS Services Used
- Amazon EC2
- Amazon S3
- AWS IAM
- Security Groups
- EC2 Key Pair
- boto3 (AWS SDK for Python)

---

## 🏗 Architecture
Python boto3 Script → AWS APIs → EC2 / S3 / Key Pair Resources

---

## 🚀 Implementation Steps

### Step 1: Configured AWS Credentials
- Configured IAM user and access permissions
- Connected AWS account using boto3

### Step 2: Created EC2 Key Pair
- Generated EC2 Key Pair using Python script
- Downloaded and stored `.pem` file securely

### Step 3: Created Security Group
- Allowed SSH and HTTP access
- Configured inbound rules

### Step 4: Provisioned EC2 Instance
- Launched EC2 instance programmatically
- Attached created Key Pair and Security Group

### Step 5: Created S3 Bucket
- Automated S3 bucket creation using boto3

### Step 6: Verified Resources
- Checked created resources in AWS Console
- Verified successful script execution

---

## 📸 Screenshots Included
- boto3 Script Execution
- Key Pair Created
- Security Group Configuration
- EC2 Instance Running
- S3 Bucket Created

---

## ✅ Project Outcome
Successfully automated AWS resource provisioning using Python boto3 scripts including EC2 Key Pair creation and infrastructure deployment.
