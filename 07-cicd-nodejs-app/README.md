# CI/CD Pipeline to Deploy Node.js Application

## 📌 Project Overview
This project demonstrates how to implement a CI/CD pipeline for a Node.js application using AWS services.

The pipeline automatically builds and deploys the application whenever code changes are pushed, reducing manual deployment effort and enabling continuous delivery.

---

## 🎯 Objective
- Automate Node.js application deployment
- Implement Continuous Integration and Continuous Deployment
- Reduce manual deployment tasks
- Improve deployment efficiency

---

## 🧰 AWS Services Used
- AWS CodePipeline
- AWS CodeBuild
- Amazon EC2 / Amazon S3
- AWS IAM
- boto3 (AWS SDK for Python)

---

## 🏗 Architecture
Source Code → CodePipeline → CodeBuild → EC2 / S3 Deployment

---

## 🚀 Implementation Steps

### Step 1: Created Node.js Application
- Developed sample Node.js application
- Configured project dependencies

### Step 2: Configured Build Process
- Created `buildspec.yml`
- Configured build commands for CodeBuild

### Step 3: Created CI/CD Pipeline
- Configured AWS CodePipeline stages
- Connected source, build, and deployment stages

### Step 4: Automated AWS Setup
- Used Python boto3 scripts for AWS resource provisioning

### Step 5: Tested Deployment
- Triggered pipeline execution
- Verified automatic deployment

---

## 📸 Screenshots Included
- Node.js Application Code
- iam role created
- CodePipeline Created
- CodeBuild Configuration
- Pipeline Execution Success
- Deployment Output

---

## ✅ Project Outcome
Successfully implemented an automated CI/CD pipeline for deploying a Node.js application using AWS services.
