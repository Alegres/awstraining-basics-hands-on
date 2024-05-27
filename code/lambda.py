import json
import boto3
import logging
import os

# Configure logging​
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Get SNS topic ARN from env variable
sns_topic_arn = os.getenv('SNS_TOPIC_ARN')

# Create SNS client​
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':  # React only on PutItem events​
            # Extract the item data from the event​
            item_data = record['dynamodb']['NewImage']

            # Convert the data to JSON​
            json_data = json.dumps(item_data)

            # Publish the item data to SNS topic​
            response = sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=json_data
            )

            # Log the published item and response​
            logger.info("Published item to SNS topic: %s", response)