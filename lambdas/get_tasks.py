import boto3
import json

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('TasksTable')

def lambda_handler(event, context):
    try:
        response = table.scan()  
        items = response.get('Items', [])

        return {
            "statusCode": 200,
            "body": json.dumps({"tasks": items})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Could not fetch tasks", "details": str(e)})
        }
