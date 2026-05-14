# Scalable Web App with ALB and Auto Scaling

## 📌 Project Overview
This project demonstrates how to deploy a scalable and highly available web application on AWS using EC2, Application Load Balancer (ALB), and Auto Scaling Group.

The load balancer distributes incoming traffic across multiple EC2 instances, while Auto Scaling automatically increases or decreases the number of servers based on CPU utilization.

---

## 🎯 Objective
- Handle high traffic automatically
- Ensure high availability
- Distribute traffic using ALB
- Automatically scale EC2 instances based on load

---

## 🧰 AWS Services Used
- Amazon EC2
- Application Load Balancer (ALB)
- Auto Scaling Group
- Launch Template
- Amazon Machine Image (AMI)
- Security Groups
- CloudWatch Monitoring

---

## 🏗 Architecture
User → ALB → Auto Scaling Group → EC2 Instances

---

## 🚀 Implementation Steps

### Step 1: Created EC2 Instances
- Launched two Amazon Linux 2 EC2 instances
- Configured Security Group for SSH (22) and HTTP (80)
- Installed Apache Web Server using User Data

### Step 2: Configured Web Server
- Installed and started Apache (`httpd`)
- Created sample HTML page displaying hostname

### Step 3: Created Target Group
- Configured HTTP Target Group on Port 80
- Registered EC2 instances
- Verified healthy status

### Step 4: Created Application Load Balancer
- Configured Internet-facing ALB
- Attached Target Group
- Selected two availability zones/subnets

### Step 5: Tested Load Balancing
- Accessed ALB DNS URL
- Verified traffic distribution between servers

### Step 6: Created AMI
- Created custom AMI from configured EC2 instance

### Step 7: Created Launch Template
- Used custom AMI
- Configured instance type and security group

### Step 8: Created Auto Scaling Group
- Attached Launch Template
- Connected to existing Target Group
- Configured desired, minimum, and maximum capacity

### Step 9: Configured Scaling Policy
- Used Target Tracking Policy
- CPU Utilization target set to 50%

### Step 10: Tested Auto Scaling
- Generated CPU load using stress tool
- Verified automatic instance creation

---

## 📸 Screenshots Included
- EC2 Instances
- Target Group Health Check
- Application Load Balancer
- Auto Scaling Group
- Launch Template
- Scaling Policy
- CloudWatch Monitoring
- Auto Scaling Activity
- Terminal Commands and Outputs

---

## ✅ Project Outcome
Successfully implemented a scalable AWS web application infrastructure using ALB and Auto Scaling. The system automatically distributes traffic and scales resources based on workload.

---
