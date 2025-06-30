#!/bin/bash
set -e

# Install requirements if the file exists
if [ -e "/opt/airflow/requirements.txt" ]; then
  $(command python) -m pip install --upgrade pip
  $(command -v pip) install --user -r /opt/airflow/requirements.txt
fi

$(command -v pip) install --user kafka-python

# Initialize the database if it doesn't exist
if [ ! -f "/opt/airflow/airflow.db" ]; then
  airflow db init && \
  airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Upgrade the database
$(command -v airflow) db upgrade

# Start the Airflow webserver and scheduler
airflow webserver & 
airflow scheduler &

# Execute the passed command
exec airflow "$@"
