# AWS Automation Projects with Boto3

A collection of hands-on AWS automation projects built using Python and Boto3. This repository demonstrates practical experience with cloud infrastructure automation, serverless architectures, and data pipelines on AWS.

The goal of this workspace is to practice building real-world AWS workflows using infrastructure scripting instead of manual console operations.

## Overview

This repository contains multiple mini-projects that automate different AWS services using Python and the AWS SDK (Boto3).

Key concepts implemented:
- Cloud Infrastructure Automation
- Serverless Architecture
- Event-Driven Systems
- Data Processing Pipelines
- AWS SDK Programming

## Architecture Example

Example pipeline implemented in this repository:

```
JSON Student Data
      ↓
Amazon S3
      ↓
Python Script (Boto3)
      ↓
Filter Students (Marks > 40)
      ↓
Amazon DynamoDB
```

Serverless image processing pipeline:

```
Image Upload
      ↓
Amazon S3
      ↓
S3 Event Trigger
      ↓
AWS Lambda
      ↓
Amazon Rekognition
      ↓
Processed Output
```

## AWS Services Used

| Service | Purpose |
|---------|---------|
| Amazon S3 | Object storage and data ingestion |
| AWS Lambda | Serverless compute |
| Amazon DynamoDB | NoSQL database |
| Amazon Rekognition | Image and face detection |
| Amazon Polly | Text-to-speech |
| Amazon EC2 | Virtual compute instances |
| AWS IAM | Identity and access management |
| Amazon EventBridge | Scheduled automation |

## Project Structure

```
AWS-Boto3
│
├── AWS_polly
├── DynamoDB
├── DynamoDBTask
├── EC2
├── IAM
├── Lambda_function_withS3
├── lambda_project
├── Monitoring_System
├── rekognition_project
├── S3
├── S3_lambda_JPG
├── serverless_face_detection
└── Tasks
```

Each directory contains automation scripts for a specific AWS service or architecture pattern.

## Key Projects

### S3 Automation

Scripts demonstrating Amazon S3 operations using Boto3.

Features implemented:
- Bucket creation
- File uploads
- File downloads
- JSON data storage
- Searching files
- Dictionary data storage

Example scripts:
- `create_bucket.py`
- `uploadingfile.py`
- `searching.py`
- `dictionary.py`
- `jsonUserInput.py`

### DynamoDB Operations

Automating operations on Amazon DynamoDB.

Features:
- Table creation
- Insert records
- Read records
- Update records
- Delete records
- Batch operations
- Data filtering

Example scripts:
- `BatchOP.py`
- `DeleteOP.py`
- `updateOP.py`
- `readOP.py`
- `pass-fail.py`
- `80-above.py`

Student database use cases implemented:
- Pass / Fail calculation
- Marks filtering
- Bulk record updates
- Conditional deletion

### S3 to DynamoDB Data Pipeline

**Folder:** `DynamoDBTask`

Implements a data ingestion pipeline.

Steps:
1. Create S3 bucket
2. Generate student JSON data
3. Upload JSON file to S3
4. Create DynamoDB table
5. Read JSON from S3
6. Insert filtered records into DynamoDB

Condition used: Insert only students with marks greater than 40

Files:
- `1_create_bucket.py`
- `2_create_json_file.py`
- `3_upload_to_s3.py`
- `4_create_dynamodb_table.py`
- `5_read_s3_insert_dynamodb.py`

### AWS Lambda Projects

Automating Lambda deployments and triggers.

Features:
- Lambda creation via Boto3
- Code deployment using zip packages
- Function invocation
- Trigger configuration

Files:
- `create_lambda.py`
- `deploy.py`
- `invoke_lambda.py`
- `lambda_function.py`

### Lambda + S3 Event System

**Folder:** `S3_lambda_JPG`

Architecture:
```
Upload Image
      ↓
Amazon S3
      ↓
S3 Event Notification
      ↓
AWS Lambda
      ↓
Processing
```

### Image Processing with Rekognition

**Folder:** `rekognition_project`

Features:
- Face detection
- Bounding box visualization
- Image analysis

Scripts:
- `detect_faces.py`
- `detect_and_draw.py`

### Serverless Face Detection System

**Folder:** `serverless_face_detection`

Architecture:
```
Image Upload
     ↓
Amazon S3
     ↓
Lambda Trigger
     ↓
Amazon Rekognition
```

This demonstrates event-driven serverless architecture.

### Text to Speech with AWS Polly

**Folder:** `AWS_polly`

Features:
- Text to speech conversion
- Multiple voice support
- Audio file generation
- S3 storage of audio output

Scripts:
- `lambda_function.py`
- `multi_voice_s3_polly.py`
- `s3_polly_full_pipeline.py`

### EC2 Automation

**Folder:** `EC2`

Automating EC2 infrastructure using Boto3.

Example: `creatingInstance.py`

Features:
- Instance creation
- Key pair usage
- Instance configuration

### IAM Automation

**Folder:** `IAM`

Scripts for managing AWS Identity and Access Management.

Features:
- Creating users
- Managing permissions
- Authorization automation

Scripts:
- `Operations.py`
- `S3ops.py`
- `userAuthorization.py`

### Monitoring System (Lambda + EventBridge)

**Folder:** `Monitoring_System`

Implements scheduled monitoring using EventBridge and Lambda.

Architecture:
```
EventBridge Scheduler
         ↓
Lambda Function
         ↓
Health Monitoring
```

Files:
- `create_lambda_boto3.py`
- `create_schedule.py`
- `health_lambda.py`

## Technologies Used

- Python
- Boto3
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon Rekognition
- Amazon Polly
- AWS IAM
- Amazon EC2
- Amazon EventBridge

## Skills Demonstrated

This repository demonstrates experience with:
- AWS Cloud Automation
- Boto3 Programming
- Serverless Application Design
- Cloud Data Pipelines
- Event-Driven Architecture
- NoSQL Database Operations
- Infrastructure Scripting
- Image Processing on AWS
- Text-to-Speech Systems

## How to Run Scripts

1. Install dependencies:
```bash
pip install boto3
```

2. Configure AWS credentials:
```bash
aws configure
```

3. Run scripts:
```bash
python script_name.py
```

## Author

Rohit Jadhav

GitHub: [https://github.com/rohitjadhav07](https://github.com/rohitjadhav07)

Repository: [https://github.com/rohitjadhav07/AWS-Boto3](https://github.com/rohitjadhav07/AWS-Boto3)
