# 🚀 AWS Serverless Image Processing Platform



> **An event-driven serverless application that automatically resizes uploaded images using AWS Lambda and stores the processed images back into Amazon S3 while sending real-time email notifications through Amazon SNS.**

---
<img width="1536" height="1024" alt="architecture-diagram png" src="https://github.com/user-attachments/assets/5b6a54cd-63f5-46a4-9cb4-222be74b5a4a" />

## 📖 Project Overview

Modern cloud applications should respond automatically to events without requiring dedicated servers. This project demonstrates how AWS Serverless services can be combined to build a scalable, automated image processing pipeline.

Whenever a user uploads an image into an Amazon S3 bucket, the application automatically:

- Detects the uploaded image
- Invokes an AWS Lambda function
- Resizes the image using the Pillow library
- Stores the processed image in another folder
- Sends an email notification using Amazon SNS
- Records execution logs in Amazon CloudWatch

This project showcases how event-driven architectures can eliminate manual intervention while providing scalability, reliability, and low operational overhead.

---

## 🎯 Project Objectives

- Build a fully serverless image processing application.
- Learn AWS event-driven architecture.
- Automate image resizing using AWS Lambda.
- Store original and processed images in Amazon S3.
- Implement email notifications using Amazon SNS.
- Monitor application execution using Amazon CloudWatch.
- Apply IAM best practices for secure service communication.

---

# 🏗️ Solution Architecture

```
                User
                  │
                  ▼
        Upload Image (.jpg)
                  │
                  ▼
          Amazon S3 Bucket
            uploads/
                  │
                  ▼
        S3 Event Notification
                  │
                  ▼
         AWS Lambda Function
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
Resize Image             Amazon SNS
      │                       │
      ▼                       ▼
processed/              Email Notification
      │
      ▼
Amazon CloudWatch Logs
```

---

# ⚙️ AWS Services Used

| Service | Purpose |
|----------|---------|
| Amazon S3 | Store original and processed images |
| AWS Lambda | Execute image processing logic |
| AWS IAM | Secure service permissions |
| Amazon SNS | Send email notifications |
| Amazon CloudWatch | Monitor logs and execution |
| Lambda Layer | Package the Pillow library |

---

# ✨ Key Features

- Event-driven image processing
- Fully serverless architecture
- Automatic image resizing
- Email notifications
- CloudWatch logging
- Secure IAM Role configuration
- Lambda Layer for dependency management
- Scalable and cost-effective solution

---

# 🔄 Project Workflow

1. User uploads an image to the **uploads/** folder in Amazon S3.
2. Amazon S3 generates an Object Created event.
3. The event triggers the AWS Lambda function.
4. Lambda downloads the uploaded image.
5. The Pillow library resizes the image.
6. The processed image is uploaded to the **processed/** folder.
7. Amazon SNS sends an email notification.
8. CloudWatch records execution logs.

---

# 📂 Project Structure

```text
aws-serverless-image-processing/

├── README.md
├── LICENSE
├── .gitignore
│
├── lambda/
│   ├── lambda_function.py
│   └── requirements.txt
│
├── docs/
│   ├── deployment-guide.md
│   ├── architecture.md
│   └── troubleshooting.md
│
├── architecture/
│   └── architecture-diagram.png
│
├── screenshots/
│
└── images/
```
---

# 🏛️ Architecture Highlights

This project follows an **event-driven serverless architecture**, where AWS services communicate automatically without requiring dedicated servers.

### Key Design Decisions

- Event-driven processing using Amazon S3 Event Notifications
- Fully serverless compute using AWS Lambda
- Secure access management with IAM Roles
- Dependency management using Lambda Layers
- Automatic notifications through Amazon SNS
- Centralized logging with Amazon CloudWatch

---

# 🚀 Deployment Guide

Follow these steps to deploy the project:

### Step 1

Create an IAM Role for Lambda.

Attach appropriate permissions for:

- Amazon S3
- Amazon SNS
- CloudWatch Logs

---

### Step 2

Create an Amazon S3 bucket.

Inside the bucket create two folders.

```
uploads/
processed/
```

---

### Step 3

Create an Amazon SNS Topic.

Subscribe your email address and confirm the subscription.

---

### Step 4

Create the Pillow Lambda Layer.

Attach the layer to the Lambda Function.

---

### Step 5

Create the Lambda Function.

Configure:

- Runtime
- IAM Role
- Environment Variables
- Lambda Layer

---

### Step 6

Configure Amazon S3 Event Notification.

Trigger:

Object Created

Prefix:

```
uploads/
```

Suffix:

```
.jpg
```

Destination:

AWS Lambda

---

### Step 7

Upload an image inside

```
uploads/
```

The application will automatically process the image.

---

# ✅ Verification

Successful deployment can be verified by checking:

- Processed image available in **processed/**
- SNS email received
- CloudWatch execution logs generated
- Lambda invocation successful

---

# 💼 Skills Demonstrated

This project demonstrates practical experience with:

- Amazon S3
- AWS Lambda
- Lambda Layers
- Amazon SNS
- Amazon CloudWatch
- IAM Roles & Policies
- Event-Driven Architecture
- Serverless Computing
- Python Automation
- Cloud Monitoring

---

# 📈 Future Enhancements

Future improvements planned for this project:

- Support PNG and WebP images
- Image compression
- Watermarking
- Image metadata extraction
- Multiple image resolutions
- Infrastructure as Code using Terraform
- CI/CD deployment using Jenkins
- Containerized image processing using Docker
- Monitoring dashboard using CloudWatch Metrics

---

# 📸 Project Screenshots

The screenshots below demonstrate the successful implementation of the project.

| Screenshot | Description |
|------------|-------------|
| S3 Bucket | Bucket configuration |
| IAM Role | Lambda execution role |
| SNS Topic | Email notification service |
| Lambda Layer | Pillow dependency |
| Lambda Function | Processing logic |
| S3 Trigger | Event notification |
| CloudWatch Logs | Execution logs |
| Processed Image | Output verification |
| Email Notification | Successful processing |

---

# 📄 Project Documentation

Additional documentation is available inside the **docs/** directory.

- Deployment Guide
- Architecture Documentation
- Troubleshooting Guide

---
