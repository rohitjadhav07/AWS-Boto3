# CI/CD Pipeline for Attendance Application using AWS

## 📌 Project Overview
This project demonstrates how to automate the deployment of an Attendance Application using AWS CI/CD services and Python boto3 automation.

The pipeline automatically builds and deploys the application whenever changes are uploaded to the source storage.

---

## 🎯 Objective
- Automate Attendance Application deployment
- Implement CI/CD workflow on AWS
- Reduce manual deployment effort
- Enable continuous deployment using AWS services

---

## 🧰 AWS Services Used
- AWS CodePipeline
- AWS CodeBuild
- Amazon S3
- Amazon EC2
- AWS IAM
- boto3 (AWS SDK for Python)

---

## 🏗 Architecture
Source Files → Amazon S3 → CodePipeline → CodeBuild → Deployment

---

## 🚀 Implementation Steps

### Step 1: Created Application Files
- Prepared Attendance Application files
- Packaged application into ZIP format

### Step 2: Configured Amazon S3
- Created S3 buckets using boto3
- Uploaded application package to S3

### Step 3: Created IAM Roles
- Configured required AWS permissions
- Attached CodeBuild and CodePipeline roles

### Step 4: Configured AWS CodeBuild
- Added build configuration using `buildspec.yml`

### Step 5: Created AWS CodePipeline
- Configured automated build and deployment stages

### Step 6: Tested CI/CD Workflow
- Triggered pipeline execution
- Verified successful deployment

---

## 📸 Screenshots Included
- S3 Bucket Created
- Application ZIP Uploaded
- IAM Role Configuration
- CodeBuild Project Created
- CodePipeline Created
- Pipeline Execution Success
- Deployment Output

---

## ✅ Project Outcome
Successfully implemented an automated CI/CD pipeline for the Attendance Application using AWS services and Python boto3 automation.
