def handler(event, context):
    return {
        "statusCode": 200,
        # change this between commits to observe traffic shift
        "body": "hello from version Y"
    }
