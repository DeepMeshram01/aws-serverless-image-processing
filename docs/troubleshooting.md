# 🔧 Troubleshooting Guide

This document lists common issues you may encounter while deploying or testing the project, along with their causes and solutions.

---

# 1. Lambda Function Is Not Triggered

## Possible Causes

- S3 Event Notification is not configured.
- Incorrect prefix or suffix.
- Lambda permission issue.

## Solution

- Verify the S3 Event Notification.
- Ensure the prefix is:

```
uploads/
```

- Ensure the suffix is:

```
.jpg
```

- Confirm that the Lambda function is selected as the destination.

---

# 2. Processed Image Is Not Created

## Possible Causes

- Lambda execution failed.
- Pillow library missing.
- IAM permission denied.

## Solution

- Check Amazon CloudWatch Logs.
- Verify the Lambda Layer contains Pillow.
- Ensure the IAM Role has S3 read/write permissions.

---

# 3. Email Notification Not Received

## Possible Causes

- Email subscription not confirmed.
- Incorrect SNS Topic ARN.
- Missing SNS permission.

## Solution

- Confirm the email subscription.
- Verify the `SNS_TOPIC_ARN` environment variable.
- Ensure the Lambda role has permission to publish to Amazon SNS.

---

# 4. Access Denied Error

## Possible Causes

- Missing IAM permissions.

## Solution

Verify that the Lambda execution role has permissions for:

- Amazon S3
- Amazon SNS
- Amazon CloudWatch Logs

---

# 5. No Module Named 'PIL'

## Possible Causes

- Pillow library not included.

## Solution

- Rebuild the Lambda Layer using an AWS-compatible environment.
- Attach the updated layer to the Lambda function.

---

# 6. CloudWatch Logs Not Generated

## Possible Causes

- Missing logging permissions.

## Solution

Ensure the Lambda execution role includes CloudWatch Logs permissions.

---

# Best Practices

- Follow the principle of least privilege for IAM roles.
- Test using sample JPEG images.
- Monitor CloudWatch Logs after each deployment.
- Remove unused AWS resources to avoid unnecessary charges.
