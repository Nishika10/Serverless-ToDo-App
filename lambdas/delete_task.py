import boto3
import json

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = "TasksTable"

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    # Parse JSON input
    body = json.loads(event['body'])
    task_id = body['taskId']

    try:
        table.delete_item(
            Key={'taskId': task_id}
        )

        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Task deleted successfully!"})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
