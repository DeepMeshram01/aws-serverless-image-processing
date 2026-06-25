import os
import json
import boto3
from PIL import Image

s3 = boto3.client("s3")
sns = boto3.client("sns")

SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]
OUTPUT_PREFIX = os.environ["OUTPUT_PREFIX"]


def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    filename = os.path.basename(key)

    download_path = f"/tmp/{filename}"
    output_path = f"/tmp/resized-{filename}"

    print(f"Downloading {key}")

    s3.download_file(bucket, key, download_path)

    image = Image.open(download_path)

    image.thumbnail((800, 800))

    image.save(output_path)

    output_key = OUTPUT_PREFIX + "resized-" + filename

    s3.upload_file(output_path, bucket, output_key)

    message = f"""
Image Processing Completed Successfully

Bucket : {bucket}

Original Image : {key}

Processed Image : {output_key}
"""

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Image Processing Completed",
        Message=message
    )

    print("Processing completed successfully")

    return {
        "statusCode": 200,
        "body": json.dumps("Success")
    }
