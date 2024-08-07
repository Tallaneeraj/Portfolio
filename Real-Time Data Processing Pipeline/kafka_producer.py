import requests, uuid, logging
from kafka import KafkaProducer
import json
import time


producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    try:
        data = {}
        location = res['location']
        data['id'] = str(uuid.uuid4())
        data['first_name'] = res['name']['first']
        data['last_name'] = res['name']['last']
        data['gender'] = res['gender']
        data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                        f"{location['city']}, {location['state']}, {location['country']}"
        data['post_code'] = location['postcode']
        data['email'] = res['email']
        data['username'] = res['login']['username']
        data['dob'] = res['dob']['date']
        data['registered_date'] = res['registered']['date']
        data['phone'] = res['phone']
        data['picture'] = res['picture']['medium']
        return data
    
    except KeyError as e:
        logging.error(f"Failed to format data: {e}")
        raise
    


def produce_messages():
    for _ in range(10): # 12 iterations to cover 60 seconds (5 seconds per iteration)
        data = get_data()
        data = format_data(data)
        producer.send('info_topic', data)
        print(f'Sent: {data}')
        time.sleep(10)  # Fetch data every minute

if __name__ == "__main__":
    produce_messages()
