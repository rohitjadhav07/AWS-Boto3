# Automated AWS Cost Optimizer using Lambda and CloudWatch

## 📌 Project Overview
This project demonstrates how to automatically reduce AWS infrastructure costs by stopping idle EC2 instances using AWS Lambda and Amazon CloudWatch.

The system monitors EC2 CPU utilization and automatically triggers a Lambda function to stop idle instances when CPU usage remains below the defined threshold.

---

## 🎯 Objective
- Detect idle EC2 instances automatically
- Reduce unnecessary AWS costs
- Automate EC2 management using AWS services
- Improve cloud resource efficiency

---

## 🧰 AWS Services Used
- AWS Lambda
- Amazon CloudWatch
- Amazon EC2
- AWS IAM

---

## 🏗 Architecture
EC2 → CloudWatch Alarm → Lambda Function → Stop EC2 Instance

---

## 🚀 Implementation Steps

### Step 1: Created IAM Role
- Configured Lambda execution role
- Attached EC2 access permissions

### Step 2: Created Lambda Function
- Developed Python Lambda function
- Configured EC2 stop automation

### Step 3: Configured CloudWatch Alarm
- Monitored EC2 CPU utilization
- Triggered Lambda when CPU usage became low

### Step 4: Tested Automation
- Triggered Lambda function
- Verified automatic EC2 shutdown

### Step 5: Added EC2 Tags
- Configured AutoStop tag for safe automation

---

## 📸 Screenshots Included
- IAM Role Configuration
- Lambda Function Created
- Lambda Code Deployment
- CloudWatch Alarm Configuration
- EC2 Running State
- EC2 Stopped State
- Lambda Logs Output

---

## ✅ Project Outcome
Successfully implemented an automated AWS cost optimization solution that automatically stops idle EC2 instances using Lambda and CloudWatch.
