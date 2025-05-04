Overview
This project is a high-throughput real-time data streaming pipeline capable of processing 1 billion queries per hour using Apache Kafka, Apache Spark, and Cassandra, orchestrated with Docker and monitored via Prometheus and Grafana. It is designed for high scalability and efficient aggregation, ensuring low-latency data processing and storage optimization.
Technical Specifications
Data Generation & Optimization:


Initially, Python was used for data generation but was limited to ~1K records/sec (single-threaded) and ~8K records/sec (with 3 threads).
Switched to Java with 3 threads, achieving 30,000 records per second, enabling 1 billion queries per hour.
Data Throughput:


Each query size: ~120 bytes
30,000 queries per second → 1 billion queries per hour
Total raw data stored in Cassandra for 1 hour: ~100GB
Data Aggregation Strategy:


Aggregated metrics (every 30 seconds) include:
Count of transactions
Total transaction amount, grouped by merchant ID
Number of merchants: 3
Resultant data entries stored in Cassandra per hour: 3 × 2 (updates per min) × 60 = 360 entries
Storage footprint for aggregated data: ~36KB
Monitoring & Alerting:
Prometheus & Grafana used for real-time system monitoring.
Alerting Conditions:
If Kafka message lag exceeds a threshold.
If processing latency in Spark crosses 1 second per batch.
If Cassandra write failures or query response time exceeds acceptable limits.
This project demonstrates optimizing real-time data generation, processing, and storage while ensuring efficient monitoring. 🚀
