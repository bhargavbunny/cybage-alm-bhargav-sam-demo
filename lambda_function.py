import boto3
import time

def lambda_handler(event, context):
    ssmClient = boto3.client('ssm')
    instanceId = "i-0e4e5379df2db213f"
    message = event['Records'][0]['Sns']['Message']
    if message == "yes":
        print("Message From SNS: " + message)
        ssmCommand = ssmClient.send_command(
            InstanceIds=[
                instanceId
            ],
            DocumentName='cybage-alm-bhargav-allow-port',
            OutputS3BucketName="bhargav-alm-ssm"
        )
    elif message == "no":
        print("Message From SNS: " + message)
        ssmCommand = ssmClient.send_command(
            InstanceIds=[
                instanceId
            ],
            DocumentName='cybage-alm-bhargav-block-port'
        )
    else:
        ssmCommand = ssmClient.send_command(
            InstanceIds=[
                instanceId
            ],
            DocumentName='cybage-alm-bhargav-allow-port'
        )
