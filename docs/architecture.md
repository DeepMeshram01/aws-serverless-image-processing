# 🏗️ Architecture

## Overview

This project follows an event-driven serverless architecture.

Whenever a user uploads an image into the `uploads/` folder of Amazon S3, the upload event automatically invokes an AWS Lambda function.

The Lambda function processes the image, stores the resized version in the `processed/` folder, sends an email notification using Amazon SNS, and records execution details in Amazon CloudWatch Logs.

---

## Architecture Flow

```
User
   │
   ▼
Amazon S3 (uploads/)
   │
   ▼
S3 Event Notification
   │
   ▼
AWS Lambda
   │
   ├────────► Amazon SNS
   │              │
   │              ▼
   │        Email Notification
   │
   ▼
Amazon S3 (processed/)
   │
   ▼
Amazon CloudWatch Logs
```

---

## AWS Services Used

- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon SNS
- Amazon CloudWatch
- Lambda Layers

---

## Benefits

- Fully Serverless
- Event-Driven
- Automatic Processing
- Cost Effective
- Highly Scalable
- Low Operational Overhead
