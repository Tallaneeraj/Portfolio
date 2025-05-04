# 📊 Data Ingestion using AWS

## 📝 Overview
This project demonstrates a real-time data ingestion and processing pipeline built entirely with AWS services. It ingests streaming data using Amazon Kinesis, processes it using AWS Lambda and AWS Glue, stores it in Amazon S3, and orchestrates the workflow using AWS Step Functions. CloudWatch is used to monitor the pipeline for performance and reliability.

The pipeline is designed for scalability and real-time performance, enabling efficient data collection and transformation for analytics or storage.

---

## 🚀 Features

- **Real-time Data Ingestion:** Streams incoming data using Amazon Kinesis Data Streams.
- **Serverless Processing:** Uses AWS Lambda for lightweight data processing tasks.
- **ETL and Transformation:** Processes and transforms data using AWS Glue.
- **Data Storage:** Stores raw and transformed data in Amazon S3.
- **Orchestration:** AWS Step Functions orchestrate the complete workflow.
- **Monitoring:** CloudWatch logs and metrics provide visibility into data flow and performance.

---

## 🧱 Architecture

- **AWS Kinesis:** Ingests streaming data from producers (e.g., sensors, logs).
- **AWS Lambda:** Consumes data from Kinesis, performs basic processing, and stores it in S3.
- **AWS Glue:** Transforms raw data into structured formats (e.g., Parquet) for querying or downstream use.
- **Amazon S3:** Stores raw and processed data.
- **AWS Step Functions:** Coordinates Lambda and Glue operations as part of a defined workflow.
- **CloudWatch:** Monitors Lambda executions, Glue jobs, and Kinesis metrics.

---

## ⚙️ Technologies Used

- **AWS Kinesis Data Streams**
- **AWS Lambda (Python)**
- **AWS Glue (ETL Jobs)**
- **Amazon S3**
- **AWS Step Functions**
- **Amazon CloudWatch**
- **Boto3 (Python SDK for AWS)**

---

## 🧪 Sample Use Case

 A sensor system generates real-time temperature data. The data is streamed via Kinesis, minimally processed and validated by a Lambda function, stored in S3, transformed by a Glue job, and orchestrated using Step Functions. This enables near real-time analytics on streaming sensor data.

---

## 🔧 Setup Instructions

1. **Create AWS Resources**:
   - Kinesis Stream (e.g., `RealTimeStream`)
   - S3 Bucket for raw and processed data
   - Lambda Function with permissions to read from Kinesis and write to S3
   - Glue Crawler and Job
   - Step Functions state machine
   - CloudWatch for monitoring

2. **Deploy Lambda Function**:
   - Add the function code to AWS Lambda
   - Attach trigger from Kinesis stream

3. **Create and Run Glue Crawler and Job**:
   - Create a Crawler for the S3 bucket
   - Write and run a Glue job for data transformation

4. **Define Step Functions Workflow**:
   - Create a JSON ASL definition that invokes the Lambda function and Glue job

5. **Monitor Pipeline**:
   - Use CloudWatch to view logs, set alarms, and track performance

---

## 📂 Project Structure

```plaintext
├── lambda/
│   └── lambda_handler.py         # Processes data from Kinesis and stores in S3
├── glue/
│   └── glue_script.py            # Transforms and writes data to S3 in structured format
├── step-functions/
│   └── state_machine.json        # ASL definition for the Step Functions workflow
├── producer/
│   └── producer.py               # Sample Kinesis producer to simulate streaming data
└── README.md

