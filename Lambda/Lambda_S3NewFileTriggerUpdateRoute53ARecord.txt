import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    FileName = event["Records"][0]["s3"]["object"]["key"]
    
    if FileName == "ip.txt" :
    
        obj = s3.get_object(Bucket=bucket, Key=FileName)
        filedata = obj['Body'].read()

        ip = filedata.decode('utf-8')
        
        print(ip)
    
        route = boto3.client('route53')
        zone_id = '/hostedzone/Z0925745372ASHROW8CFX'

        boto3.set_stream_logger('botocore')
        response = route.change_resource_record_sets(
			HostedZoneId=zone_id,
			ChangeBatch={
				'Changes': [
					{
						'Action': 'UPSERT',
						'ResourceRecordSet': {
							'Name': 'jorisdieltiens.com',
							'ResourceRecords': [
								{
									'Value': ip
								}
							],
							'Type': 'A',
							'TTL': 900
						}
					}
				]
			}
		)
