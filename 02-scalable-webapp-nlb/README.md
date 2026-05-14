# Scalable Web App with NLB and Auto Scaling

## 📌 Project Overview
This project demonstrates how to deploy a scalable and high-performance web application on AWS using Network Load Balancer (NLB) and Auto Scaling Group.

The NLB distributes TCP traffic across multiple EC2 instances, while Auto Scaling automatically launches or terminates instances based on CPU utilization.

---

## 🎯 Objective
- Handle high traffic with low latency
- Distribute traffic using NLB
- Automatically scale EC2 instances
- Improve application availability

---

## 🧰 AWS Services Used
- Amazon EC2
- Network Load Balancer (NLB)
- Auto Scaling Group
- Launch Template
- Target Group
- Security Groups

---

## 🏗 Architecture
User → NLB → Auto Scaling Group → EC2 Instances

---

## 🚀 Implementation Steps

### Step 1: Created Launch Template
- Configured Amazon Linux EC2 template
- Added User Data to install Apache server
- Configured Security Group for SSH and HTTP

### Step 2: Created Target Group
- Protocol: TCP
- Port: 80
- Configured health checks

### Step 3: Created Network Load Balancer
- Internet-facing NLB
- Attached target group
- Selected multiple subnets

### Step 4: Created Auto Scaling Group
- Attached launch template
- Connected to NLB target group
- Configured desired, minimum, and maximum capacity

### Step 5: Configured Scaling Policy
- Target tracking policy
- CPU utilization threshold: 50%

### Step 6: Tested Load Balancing and Scaling
- Accessed NLB DNS in browser
- Verified traffic distribution
- Increased instance count using Auto Scaling

---

## 📸 Screenshots Included
- Launch Template
- Network Load Balancer
- Target Group Healthy Status
- Auto Scaling Group
- Running EC2 Instances
- Browser Output
- Scaling Activity

---

## ✅ Project Outcome
Successfully deployed a scalable AWS infrastructure using Network Load Balancer and Auto Scaling for handling high-performance traffic efficiently.
