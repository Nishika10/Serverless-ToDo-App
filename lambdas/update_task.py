import boto3
import json

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = "TasksTable"

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    # Parse JSON input
    body = json.loads(event['body'])

    task_id = body['taskId']
    new_title = body['title']
    new_status = body['status']

    try:
        response = table.update_item(
            Key={'taskId': task_id},
            UpdateExpression="SET title = :t, #st = :s",
            ExpressionAttributeNames={
                "#st": "status"  # because 'status' is a reserved word
            },
            ExpressionAttributeValues={
                ':t': new_title,
                ':s': new_status
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Task updated successfully!"})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
