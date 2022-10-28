import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = "tmcloud"
    fileName = event["queryStringParameters"]["name"]
    uploadByteStraem = bytes(event["queryStringParameters"]["content"].encode("UTF-8"))
    
    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStraem)
    
    return {
        'statusCode': 200,
        'body': json.dumps(event["queryStringParameters"]["ip"])
    }

