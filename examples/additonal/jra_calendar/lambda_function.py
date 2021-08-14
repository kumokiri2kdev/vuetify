import boto3
import json
import server_logic

AWS_S3_BUCKET_NAME = 'jracalendar'
s3 = boto3.resource('s3')
bucket = s3.Bucket(AWS_S3_BUCKET_NAME)


def handle_api(event):
    month = event['queryStringParameters']['month']

    obj = bucket.Object('kaisai.json')
    response = obj.get()
    body = response['Body'].read().decode('utf-8')

    events = json.loads(body)

    if month in events:
        event = server_logic.filtering(events[month])
    else:
        event = []

    ret = {
        'statusCode': 200,
        'headers':{
            'Content-Type':'application/json'
        },
        'body': json.dumps(event, ensure_ascii=False)
    }

    return ret

def lambda_handler(event, context):
    if event['resource'] == '/api/{apiname}':
        ret = handle_api(event)
    else:
        obj = bucket.Object('index.html')
        response = obj.get()
        body = response['Body'].read()
        html = body.decode('utf-8')

        ret = {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": html
        }

    return ret

if __name__ == '__main__':
    event_html = {
        "resource": "/index.html",
    }

    event_api = {
        "resource": "/api/{apiname}",
        "pathParameters": {
            "apiname": "event"
        },
        "queryStringParameters": {
            "month": "202108"
        },
    }

    ret = lambda_handler(event_html, None)
    print(ret)
