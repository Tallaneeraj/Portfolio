# 🚀 StreamScale – Real-Time Billion Query Processing Pipeline

StreamScale is a high-throughput, real-time data streaming pipeline capable of processing **1 billion queries per hour** using a modern big data stack: **Apache Kafka**, **Apache Spark**, and **Apache Cassandra**, orchestrated with **Docker** and monitored via **Prometheus** and **Grafana**.

---

## 📌 Project Overview

- **Goal**: Real-time processing and aggregation of massive data streams (30K queries/sec).
- **Scale**: ~1 billion queries/hour (~100GB raw data/hour).
- **Focus Areas**:
  - High-speed data generation
  - Stream processing
  - Aggregation
  - Optimized storage
  - Real-time monitoring and alerting

---

## ⚙️ Technical Specifications

### 🔄 Data Generation & Optimization

| Language | Threads | Throughput |
|----------|---------|------------|
| Python   | 1       | ~1,000 records/sec |
| Python   | 3       | ~8,000 records/sec |
| **Java** | 3       | **~30,000 records/sec** ✅ |

- Switched to multi-threaded Java-based generator to meet performance goals.

---

### 📦 Data Throughput

- **Query Size**: ~120 bytes
- **Throughput**: 30,000 queries/second
- **Total per hour**: ~1 billion queries → ~100 GB raw data stored in Cassandra

---

### 📊 Aggregation Strategy (Every 30 Seconds)

Metrics computed per merchant:
- ✅ Count of transactions
- ✅ Total transaction amount

**Aggregation math**:
- Merchants: 3  
- Aggregation Frequency: Every 30 seconds → 2 updates/min  
- Entries per hour: `3 × 2 × 60 = 360`  
- Aggregated storage per hour: ~36 KB

---

## 📡 Monitoring & Alerting

- **Monitoring Tools**: Prometheus + Grafana
- **Dashboards**: Kafka throughput, Spark batch latency, Cassandra I/O stats

### 🔔 Alert Conditions

- Kafka message lag exceeds threshold
- Spark batch latency > 1 second
- Cassandra:
  - Write failures
  - Slow query response time

---

## 🧱 Tech Stack

| Component     | Tool            |
|---------------|------------------|
| Messaging     | Apache Kafka     |
| Processing    | Apache Spark     |
| Storage       | Apache Cassandra |
| Monitoring    | Prometheus + Grafana |
| Containerization | Docker         |
| Data Generation | Java            |

---

## 🧠 Key Takeaways

- Efficient multi-threaded data generation
- Real-time processing with Spark Structured Streaming
- Scalable NoSQL storage using Cassandra
- Lightweight, high-value aggregation strategy
- Robust system observability with Prometheus & Grafana

---

## 📂 Folder Structure

