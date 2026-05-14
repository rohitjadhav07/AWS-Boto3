# Containerized Flask Application using Docker and Amazon ECS

## 📌 Project Overview
This project demonstrates how to containerize a Flask application using Docker and deploy it on Amazon ECS using AWS Fargate.

The application is packaged as a Docker container, stored in Amazon ECR, and deployed on ECS for scalable cloud-based execution.

---

## 🎯 Objective
- Containerize Python Flask application
- Deploy Docker containers on AWS
- Use Amazon ECR for image storage
- Run containers using Amazon ECS Fargate

---

## 🧰 AWS Services Used
- Amazon ECS
- Amazon ECR
- AWS Fargate
- Docker
- Python Flask

---

## 🏗 Architecture
Flask App → Docker Image → Amazon ECR → Amazon ECS → Public Access

---

## 🚀 Implementation Steps

### Step 1: Created Flask Application
- Developed simple Flask web application
- Configured application dependencies

### Step 2: Created Docker Configuration
- Added Dockerfile
- Built Docker image locally

### Step 3: Tested Docker Container
- Executed container locally using Docker
- Verified application using localhost

### Step 4: Created Amazon ECR Repository
- Configured private ECR repository
- Logged in to ECR using AWS CLI

### Step 5: Pushed Docker Image
- Tagged Docker image
- Uploaded image to Amazon ECR

### Step 6: Configured Amazon ECS
- Created ECS cluster using Fargate
- Created task definition and ECS service

### Step 7: Tested Deployment
- Accessed ECS public IP
- Verified Flask application running successfully

---

## 📸 Screenshots Included
- Dockerfile Configuration
- Docker Image Build
- Amazon ECR Repository
- Docker Push to ECR
- ECS Cluster Created
- ECS Service Running
- Final Browser Output

---

## ✅ Project Outcome
Successfully containerized and deployed a Flask application on AWS using Docker, Amazon ECR, and Amazon ECS Fargate.
