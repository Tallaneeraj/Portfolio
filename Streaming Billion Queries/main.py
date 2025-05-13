import logging, time, uuid, random, json
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

KAFKA_BROKERS = "localhost:29092,localhost:39092,localhost:49092"
NUM_PARTITIONS = 5
REPLICATION_FACTOR = 3
TOPIC_NAME = "Transaction"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

producer_conf = {
    'bootstrap.servers': KAFKA_BROKERS,
    'queue.buffering.max.messages':10000,
    'queue.buffering.max.kbytes': 512000,
    'batch.num.messages': 1000,
    'linger.ms': 10,
    'acks': 1,
    'compression.type': 'gzip'
}

producer = Producer(producer_conf)

def create_topic(topic_name):
    admit_client = AdminClient({"bootstrap.servers": KAFKA_BROKERS})

    try:
        metadata = admit_client.list_topics(timeout=10)
        if topic_name not in metadata.topics:
            topic = NewTopic(
                topic = topic_name,
                num_partitions=NUM_PARTITIONS,
                replication_factor=REPLICATION_FACTOR
            )

            fs = admit_client.create_topics([topic])
            for topic, future in fs.items():
                try:
                    future.results()
                    logger.info(f"Topics'{topic_name} created successfully!!!")
                except Exception as e:
                    logger.error(f"Failed to create topic '{topic_name}': {e}")    
        else:
            logger.info(f"Topics'{topic_name} already exists!!!") 
    except Exception as e:
        logger.error(f"Failed to creating a new topic '{topic_name}': {e}") 

def generate_transaction():
    return dict(
        transaction_id = str(uuid.uuid4()),
        userID = f"user_{random.randint(1, 100)}",
        amount = round(random.uniform(100, 150000), 2),
        transactionTime = int(time.time()),
        merchantID = random.choice(['M1', 'M2', 'M3']),
        transactionType = random.choice(['purchase', 'refund']),
        paymentMethod = random.choice(['credit_card', 'wallet', 'paypal']),
        currency = random.choice(['USD', 'Euro', 'INR'])
    )

def delivery_report(err, msg):
    if err is not None:
        logger.error(f'Delivery failed for record {msg.key()}')
    else:
        logger.info(f'Record {msg.key()} successfully produced')


if __name__ == "__main__":
    create_topic(TOPIC_NAME)

    while True:
        transaction = generate_transaction()

        try:
            producer.produce(
                topic = TOPIC_NAME,
                key = transaction['userID'],
                value=json.dumps(transaction).encode('utf-8'),
                on_delivery = delivery_report
            )
            producer.flush()


        except Exception as e:
            logger.error(f"Failed to creating a new topic:{e}")

                         
                         



