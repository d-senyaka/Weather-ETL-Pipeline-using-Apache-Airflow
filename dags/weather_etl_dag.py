from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json
import os

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 19),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define your OpenWeatherMap API Key and City
API_KEY = 'your_api_key_here'  # Replace this with your real API key
CITY = 'Colombo'

# File paths
RAW_DATA_PATH = '/home/ubuntu/airflow/data/raw_weather.json'
TRANSFORMED_DATA_PATH = '/home/ubuntu/airflow/output/transformed_data.json'

# Task 1: Extract weather data from API
def extract_weather_data():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Create data directory if not exists
    os.makedirs(os.path.dirname(RAW_DATA_PATH), exist_ok=True)

    # Save raw data
    with open(RAW_DATA_PATH, 'w') as f:
        json.dump(data, f)

# Task 2: Transform the raw data
def transform_weather_data():
    with open(RAW_DATA_PATH, 'r') as f:
        raw_data = json.load(f)

    transformed_data = {
        'city': raw_data['name'],
        'temperature': raw_data['main']['temp'],
        'humidity': raw_data['main']['humidity'],
        'weather': raw_data['weather'][0]['description'],
        'timestamp': datetime.now().isoformat()
    }

    # Create output directory if not exists
    os.makedirs(os.path.dirname(TRANSFORMED_DATA_PATH), exist_ok=True)

    # Save transformed data
    with open(TRANSFORMED_DATA_PATH, 'w') as f:
        json.dump(transformed_data, f)

# Define the DAG
with DAG(
    dag_id='weather_etl_dag',
    default_args=default_args,
    description='ETL pipeline for weather data',
    schedule_interval='@hourly',  # Can be changed as needed
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_weather',
        python_callable=extract_weather_data,
    )

    transform_task = PythonOperator(
        task_id='transform_weather',
        python_callable=transform_weather_data,
    )

    extract_task >> transform_task
