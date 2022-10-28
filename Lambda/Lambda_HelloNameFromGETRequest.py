import json

def lambda_handler(event, context):
    
    try:
        data = event["queryStringParameters"]["name"]
    except:
        data = "NoName"
    
    
    #data = json.dumps(event)
    
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps("Hallo " + data + "!")
    }
