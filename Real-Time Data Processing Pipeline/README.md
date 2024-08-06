# Real-Time Data Processing Pipeline

This project demonstrates a real-time data processing pipeline using Apache Kafka, Apache Spark, and Apache Cassandra. The pipeline fetches data from an external API, processes it, and stores it in a Cassandra database.

## Project Structure

- **kafka_producer.py**: Fetches data from the RandomUser API and sends it to a Kafka topic.
- **spark_consumer.py**: Reads data from the Kafka topic, processes it using Spark, and writes it to Cassandra.
- **docker-compose.yml**: Docker Compose file to set up Kafka, Zookeeper, Spark, and Cassandra containers.

## Technologies Used

- **Apache Kafka**: For message queuing and data streaming.
- **Apache Spark**: For real-time data processing.
- **Apache Cassandra**: For data storage.
- **Docker**: For containerization.
- **Python**: For scripting and application logic.


## Project Workflow

1. **Kafka Producer (`kafka_producer.py`):**
    - Fetches data from the [RandomUser API](https://randomuser.me/api/).
    - Formats the data and sends it to the Kafka topic `info_topic`.

2. **Spark Consumer (`spark_consumer.py`):**
    - Reads data from the Kafka topic `info_topic`.
    - Parses the JSON data and extracts necessary fields.
    - Writes the processed data to the Cassandra table `user_data` in the `user_keyspace`.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
