import json
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = 'Sensor-Data'

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['kinesis']['data'])
        filename = f"sensor-data-{int(time.time())}.json"
        s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=json.dumps(payload))
    return {'statusCode': 200, 'body': 'Success'}
