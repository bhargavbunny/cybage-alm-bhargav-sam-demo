import boto3
import time

def lambda_handler(event, context):
    ssmClient = boto3.client('ssm')
    instanceId = "i-0766f2fcbb251db11"
    message = event['Records'][0]['Sns']['Message']
    if message == "open":
        print("Message From SNS: " + message)
        ssmCommand = ssmClient.send_command(
            InstanceIds=[
                instanceId
            ],
            DocumentName='cybage-alm-bhargav-allow-port'
        )
    elif message == "close":
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
