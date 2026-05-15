# Serverless Image Resizer using AWS Lambda and Amazon S3

## 📌 Project Overview
This project demonstrates a serverless image processing system using AWS Lambda and Amazon S3.

Whenever an image is uploaded to the S3 bucket, the Lambda function automatically resizes the image and stores the resized version in another S3 bucket.

---

## 🎯 Objective
- Automatically resize uploaded images
- Implement serverless image processing
- Use AWS Lambda for automation
- Store resized images in Amazon S3

---

## 🧰 AWS Services Used
- AWS Lambda
- Amazon S3
- AWS IAM
- Lambda Layer (Pillow Library)

---

## 🏗 Architecture
Input Image → Amazon S3 → AWS Lambda → Resized Image → Output S3 Bucket

---

## 🚀 Implementation Steps

### Step 1: Created S3 Buckets
- Configured input and output image storage buckets

### Step 2: Created IAM Role
- Attached S3 and Lambda execution permissions

### Step 3: Created Lambda Function
- Developed image resizing function using Python
- Configured Pillow library layer

### Step 4: Added S3 Trigger
- Triggered Lambda automatically on image upload

### Step 5: Tested Image Resizing
- Uploaded image to S3
- Verified resized image generation

---

## 📸 Screenshots Included
- IAM Role Configuration
- Lambda Function Configuration
- Input Image Uploaded to S3
- Resized Output Image in S3

---

## ✅ Project Outcome
Successfully implemented a serverless image resizing system using AWS Lambda and Amazon S3 for automatic image processing.
