# Multi-tier Web App Deployment using AWS and boto3

## 📌 Project Overview
This project demonstrates the deployment of a multi-tier web application architecture on AWS using Python boto3 automation.

The infrastructure separates the application into:
- Frontend Layer
- Backend/Application Layer
- Database Layer

This improves scalability, security, and maintainability.

---

## 🎯 Objective
- Deploy a multi-tier architecture on AWS
- Automate AWS resource provisioning using boto3
- Separate frontend, backend, and database layers
- Improve application availability and management

---

## 🧰 AWS Services Used
- Amazon EC2
- Amazon RDS
- Application Load Balancer
- Security Groups
- boto3 (AWS SDK for Python)

---

## 🏗 Architecture
User → Load Balancer → EC2 Application Server → Amazon RDS

---

## 🚀 Implementation Steps

### Step 1: Configured AWS using boto3
- Created AWS session using Python boto3
- Configured required IAM permissions

### Step 2: Created Security Groups
- Allowed HTTP and SSH access
- Configured database access rules

### Step 3: Launched EC2 Instances
- Created frontend/application server
- Installed web server using User Data

### Step 4: Created Amazon RDS Database
- Configured MySQL database instance
- Connected backend application to RDS

### Step 5: Configured Load Balancer
- Created Application Load Balancer
- Attached EC2 instances to target group

### Step 6: Tested Application
- Verified frontend access using ALB DNS
- Verified database connectivity

---

## 📸 Screenshots Included
- boto3 Code Execution
- EC2 Instances Running
- Security Groups
- RDS Database Created
- Load Balancer Created
- Browser Output

---

## ✅ Project Outcome
Successfully deployed a scalable multi-tier web application architecture on AWS using Python boto3 automation.
