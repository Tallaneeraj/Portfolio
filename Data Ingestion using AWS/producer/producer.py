import boto3
import json
import time

kinesis = boto3.client('kinesis', region_name='us-east-1')

def produce_data():
    for i in range(10):
        data = {
            'sensor_id': f'sensor-{i}',
            'temperature': 25 + i,
            'timestamp': time.time()
        }
        kinesis.put_record(
            StreamName='RealTimeStream',
            Data=json.dumps(data),
            PartitionKey='partitionKey'
        )
        time.sleep(1)

produce_data()
