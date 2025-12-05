import json
import boto3
import datetime

dynamodb = boto3.client("dynamodb")

TABLE_NAME = "TasksTable"   # your table name

def lambda_handler(event, context):
    body = json.loads(event["body"])

    task_id = body["taskId"]
    title = body["title"]
    status = body["status"]

    created_at = datetime.datetime.utcnow().isoformat() + "Z"

    dynamodb.put_item(
        TableName=TABLE_NAME,
        Item={
            "taskId": {"S": task_id},
            "title": {"S": title},
            "status": {"S": status},
            "createdAt": {"S": created_at}
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Task added successfully!"})
    }

