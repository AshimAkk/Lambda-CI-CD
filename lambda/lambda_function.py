import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps("hello, checking if github workflow configuration is working")
    }