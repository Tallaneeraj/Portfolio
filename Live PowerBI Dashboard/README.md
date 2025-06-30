# 📊 Live Power BI Dashboard – Real-Time Streaming Data Pipeline

This project showcases a **real-time data streaming and visualization pipeline** that processes and displays live sensor data using Kafka, Spark, PostgreSQL, Airflow, Docker, and Power BI. The pipeline simulates IoT sensor readings, processes them in near real-time, and updates an interactive Power BI dashboard every 5 minutes.

---

## ⚡ Project Overview

- **Goal**: Enable real-time monitoring and analysis of sensor data (temperature and humidity) through a continuously updating dashboard.
- **Core Features**:
  - Live data ingestion and processing
  - Automated ETL pipeline
  - Near real-time dashboard with auto-refresh
- **Update Frequency**: Dashboard refreshes every 5 minutes

---

## 🏗️ Tech Stack & Architecture

### 📡 Data Source

- Python script simulates sensor data
- Generates random **temperature** and **humidity** values every second

### 💬 Apache Kafka

- Serves as a distributed message broker
- Ingests ~60 messages/minute per producer
- Supports high throughput (thousands of events per second)

### ⚙️ Apache Spark

- Spark Structured Streaming consumes Kafka data
- Batch interval: 5 seconds (near real-time)
- Performs filtering, cleaning, and aggregation

### 🗄️ PostgreSQL

- Stores processed sensor data
- Supports efficient historical and live data queries

### 🐳 Docker

- Containerizes Kafka, Spark, PostgreSQL, and Airflow
- Simplifies deployment and portability

### 🌀 Apache Airflow

- Orchestrates the entire pipeline
- DAG automates:
  - Data generation
  - Kafka producer startup
  - Spark streaming job
  - PostgreSQL data load
  - Power BI refresh trigger

### 📈 Power BI

- Connects to PostgreSQL in **DirectQuery** mode
- Auto-refreshes every 5 minutes
- Visualizes trends, anomalies, and time-series patterns

---

## 💡 Key Functionalities & Performance

### ✅ Real-Time Data Generation & Processing

- ~86,400 records generated daily
- Spark processes batches every 5 seconds for low latency
- Kafka brokers handle large event volumes seamlessly

### ✅ ETL & Database Storage

- Clean and aggregate data using Spark
- Store processed results in PostgreSQL for fast querying
- Optimized indexes for sub-200ms query responses

### ✅ Orchestration & Automation

- Airflow DAG ensures fully automated execution
- Docker Compose manages multi-container setup efficiently

### ✅ Visualization & Insights

- Power BI dashboard highlights:
  - Temperature and humidity trends
  - Anomaly alerts
  - Time-series analytics

---

## 🚧 Challenges & Solutions

- **Kafka consumer lag under high load**  
  🔧 Tuned Spark batch sizes and increased parallelism.

- **Power BI PostgreSQL connection issues (DirectQuery)**  
  🔧 Updated `pg_hba.conf`, adjusted `listen_addresses`, and configured firewall rules.

- **Spark Streaming out-of-memory errors**  
  🔧 Increased executor memory and implemented checkpointing.

---

## 📊 Results & Impact

- **Data processed per hour**: ~216,000 records
- **Query response time**: <200ms
- **Dashboard latency**: 5 minutes (near real-time)
- **Automation**: Fully automated end-to-end, no manual intervention after deployment

---

## 🚀 How This Project Relates to Data Engineering & Analytics

This project demonstrates:

- Real-time data pipeline design and optimization
- Scalable stream processing with Spark & Kafka
- Efficient data storage and querying with PostgreSQL
- Automated orchestration with Airflow
- Effective, dynamic data visualization with Power BI

---

## 🧑‍💻 Getting Started

### 🔥 Prerequisites

- Docker & Docker Compose installed
- Power BI Desktop or Power BI Service
- Python 3.x

### ⚙️ Steps

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/live-powerbi-dashboard.git
   cd live-powerbi-dashboard

