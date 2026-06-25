# 🚀 Deployment Guide

This document explains how to deploy the AWS Serverless Image Processing Platform from scratch.

---

# Prerequisites

Before deployment, ensure you have:

- An AWS Account
- IAM permissions to create AWS resources
- AWS Management Console access
- A verified email address for Amazon SNS

---

# Step 1: Create an Amazon S3 Bucket

Create an Amazon S3 bucket with a globally unique name.

Inside the bucket, create the following folders:

```
uploads/
processed/
```

---

# Step 2: Create an IAM Role

Create an IAM Role for AWS Lambda.

Attach permissions that allow the function to:

- Read objects from Amazon S3
- Write objects to Amazon S3
- Publish messages to Amazon SNS
- Write logs to Amazon CloudWatch

---

# Step 3: Create an Amazon SNS Topic

Create a new SNS Topic.

Subscribe your email address.

Confirm the subscription using the confirmation email sent by AWS.

---

# Step 4: Create the Pillow Lambda Layer

Install the Pillow library in an AWS-compatible environment.

Package it as a Lambda Layer.

Attach the layer to the Lambda function.

---

# Step 5: Create the Lambda Function

Create a new Lambda function using the Python runtime.

Configure:

- IAM Role
- Lambda Layer
- Environment Variable

Environment Variable:

```
SNS_TOPIC_ARN=<your-sns-topic-arn>
```

---

# Step 6: Configure Amazon S3 Event Notification

Create an Event Notification on the S3 bucket.

Configuration:

Event:

```
Object Created
```

Prefix:

```
uploads/
```

Suffix:

```
.jpg
```

Destination:

```
AWS Lambda
```

---

# Step 7: Test the Application

Upload a JPEG image into:

```
uploads/
```

The application will automatically:

- Invoke the Lambda function
- Resize the image
- Save the processed image
- Send an email notification
- Generate CloudWatch logs

---

# Verification Checklist

Verify the following:

- Image uploaded successfully
- Lambda invoked automatically
- Processed image available
- Email notification received
- CloudWatch logs generated

---

# Cleanup

To avoid AWS charges:

- Delete the Lambda Function
- Delete the Lambda Layer
- Delete the S3 Bucket
- Delete the SNS Topic
- Delete CloudWatch Log Groups
