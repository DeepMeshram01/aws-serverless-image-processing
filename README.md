# 🚀 AWS Serverless Image Processing Platform

> **An event-driven serverless application that automatically resizes uploaded images using AWS Lambda and stores the processed images back into Amazon S3 while sending real-time email notifications through Amazon SNS.**

---

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
