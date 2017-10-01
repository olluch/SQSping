import boto3

sqs = boto3.resource('sqs')

# Get queue by name
queue = sqs.get_queue_by_name(QueueName='test')

# Send a message
response = queue.send_message(MessageBody='hi there!')

# The response is not a resource, but gives you a message ID and MD5
print("MessageId created: {0}".format(response.get('MessageId')))
print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))

