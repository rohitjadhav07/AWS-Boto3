# Automate CI/CD Pipelines using AWS Lambda

## 📌 Project Overview
This project demonstrates how to automate CI/CD pipeline execution using AWS Lambda and AWS CodePipeline.

Whenever application files are updated, Lambda automatically triggers the deployment pipeline, enabling continuous deployment without manual intervention.

---

## 🎯 Objective
- Automate deployment workflows
- Trigger CodePipeline using AWS Lambda
- Reduce manual deployment operations
- Implement serverless CI/CD automation

---

## 🧰 AWS Services Used
- AWS Lambda
- AWS CodePipeline
- Amazon S3
- AWS IAM

---

## 🏗 Architecture
Application Upload → Amazon S3 → AWS Lambda → AWS CodePipeline → Deployment

---

## 🚀 Implementation Steps

### Step 1: Created S3 Bucket
- Configured S3 bucket for application storage

### Step 2: Created AWS Lambda Function
- Developed Lambda function to trigger pipeline execution

### Step 3: Configured CodePipeline
- Created automated deployment pipeline

### Step 4: Added S3 Trigger
- Configured Lambda trigger on S3 upload events

### Step 5: Tested Automation
- Uploaded application files to S3
- Verified automatic pipeline execution

---

## 📸 Screenshots Included
- Amazon S3 Bucket
- CodePipeline Structure
- Final Browser Output

---

## ✅ Project Outcome
Successfully implemented automated CI/CD pipeline triggering using AWS Lambda and AWS CodePipeline.
