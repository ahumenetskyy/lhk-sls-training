import json


def hw1(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
