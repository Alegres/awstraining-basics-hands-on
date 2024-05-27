#!/bin/bash
while true; do
    # Get used memory
    used_memory=$(free -m | awk 'NR==2{print $3}')

    # Create JSON request body
    current_timestamp=$(date +%s)

    echo "Current EC2 used memory: $used_memory | Timestamp: $current_timestamp" > message.txt

    # Publish message to SNS using AWS CLI
    aws sns publish --topic-arn $SNS_TOPIC_ARN --message file://message.txt

    # Wait for 120 seconds before the next iteration
    sleep 120
done