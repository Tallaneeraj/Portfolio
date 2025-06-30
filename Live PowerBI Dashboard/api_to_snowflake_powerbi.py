from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests
import json
import snowflake.connector
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Default arguments
default_args = {
    'owner': 'Neeraj',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Create Snowflake table
create_table_query = """
CREATE TABLE IF NOT EXISTS random_user_data (
    id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    gender STRING,
    dob DATE,
    registered DATE,
    country STRING,
    timestamp TIMESTAMP
)
"""

snowflake_conn_params = {
    'user': 'TALLA05',
    'password': 'NrjJanu@8500',
    'account': 'DB83870',
    'warehouse': 'my_wh',
    'database': 'mytestdb',
    'schema': 'myschema'
}

# Ensure table exists in Snowflake
def create_table():
    try:
        conn = snowflake.connector.connect(**snowflake_conn_params)
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
        conn.close()
        logging.info("Snowflake table created successfully.")
    except Exception as e:
        logging.error(f"Error creating table: {e}")

create_table()

# Define the DAG
dag = DAG(
    'api_to_snowflake_powerbi',
    default_args=default_args,
    description='Load data from API to Snowflake every second for 1 minute and refresh Power BI dashboard',
    schedule_interval=None,  # Manual trigger
    start_date=days_ago(1),
    catchup=False,
)

# Function to fetch data from the API and load it into Snowflake
def fetch_and_load_data(**kwargs):
    start_time = time.time()
    while time.time() - start_time < 60:
        response = requests.get('https://randomuser.me/api/')
        if response.status_code == 200:
            data = response.json()['results'][0]
            logging.info(f"Fetched data: {data}")
            try:
                conn = snowflake.connector.connect(**snowflake_conn_params)
                insert_query = """
                INSERT INTO random_user_data (id, first_name, last_name, email, gender, dob, registered, country, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                user_id = data['login']['uuid']
                first_name = data['name']['first']
                last_name = data['name']['last']
                email = data['email']
                gender = data['gender']
                dob = data['dob']['date']
                registered = data['registered']['date']
                country = data['location']['country']
                timestamp = datetime.utcnow()

                with conn.cursor() as cursor:
                    cursor.execute(insert_query, (
                        user_id, first_name, last_name, email, gender, dob, registered, country, timestamp
                    ))
                conn.commit()
                conn.close()
                logging.info(f"Inserted data: {data}")
            except Exception as e:
                logging.error(f"Error loading data to Snowflake: {e}")
        else:
            logging.error(f"Failed to fetch data: {response.status_code}")
        time.sleep(1)

# Function to refresh Power BI dashboard
def refresh_powerbi_dashboard(**kwargs):
    try:
        url = 'https://api.powerbi.com/v1.0/myorg/reports/{reportId}/refreshes'
        headers = {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
        }
        response = requests.post(url, headers=headers)
        if response.status_code != 202:
            logging.error(f"Failed to refresh Power BI dashboard: {response.status_code}")
        else:
            logging.info("Power BI dashboard refreshed successfully.")
    except Exception as e:
        logging.error(f"Error refreshing Power BI dashboard: {e}")

# Define tasks
fetch_load_data_task = PythonOperator(
    task_id='fetch_and_load_data',
    python_callable=fetch_and_load_data,
    dag=dag,
)

refresh_dashboard_task = PythonOperator(
    task_id='refresh_powerbi_dashboard',
    python_callable=refresh_powerbi_dashboard,
    dag=dag,
)

# Task dependencies
fetch_load_data_task >> refresh_dashboard_task
