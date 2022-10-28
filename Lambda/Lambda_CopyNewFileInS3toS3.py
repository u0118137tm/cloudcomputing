import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    FileName = event["Records"][0]["s3"]["object"]["key"]
    thumbbucket = "jdthumb"
    
    
    
    response = s3_client.get_object(Bucket=bucket, Key=FileName)
    filedata = response['Body'].read()
    
    
    response = s3_client.put_object(Bucket=thumbbucket, Key=FileName, Body=filedata)
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
