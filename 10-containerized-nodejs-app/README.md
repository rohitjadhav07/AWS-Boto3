# Containerized Node.js Application using Docker and Amazon ECS

## 📌 Project Overview
This project demonstrates how to containerize a Node.js application using Docker and deploy it on Amazon ECS using AWS Fargate.

The application is packaged into a Docker image, stored in Amazon ECR, and executed using ECS services.

---

## 🎯 Objective
- Containerize Node.js application using Docker
- Store Docker images in Amazon ECR
- Deploy containers using Amazon ECS
- Run scalable containerized applications on AWS

---

## 🧰 AWS Services Used
- Amazon ECS
- Amazon ECR
- AWS Fargate
- Docker
- Node.js

---

## 🏗 Architecture
Node.js App → Docker Image → Amazon ECR → Amazon ECS → Public Access

---

## 🚀 Implementation Steps

### Step 1: Created Node.js Application
- Developed sample Node.js web application
- Configured project dependencies

### Step 2: Created Docker Configuration
- Added Dockerfile for containerization
- Built Docker image locally

### Step 3: Created Amazon ECR Repository
- Configured private ECR repository
- Uploaded Docker image to ECR

### Step 4: Configured Amazon ECS
- Created ECS cluster using Fargate
- Created task definition and ECS service

### Step 5: Tested Deployment
- Accessed public application endpoint
- Verified successful container deployment

---

## 📸 Screenshots Included
- Dockerfile Configuration
- Amazon ECR Private Repository
- Amazon ECS Cluster
- Final Browser Output

---

## ✅ Project Outcome
Successfully containerized and deployed a Node.js application on AWS using Docker, Amazon ECR, and Amazon ECS.
