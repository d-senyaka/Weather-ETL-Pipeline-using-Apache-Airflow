# 🌤️ Weather ETL Pipeline using Apache Airflow

This project demonstrates a weather data ETL pipeline using Python and Apache Airflow. It extracts real-time weather data from the OpenWeatherMap API, transforms the data into a simplified JSON format, and stores it locally.

## 🚀 Features

- ✅ Python-based ETL pipeline
- ✅ DAGs managed with Apache Airflow
- ✅ Raw and transformed JSON outputs
- ✅ Sensors to manage data dependencies
- ✅ Modular, testable pipeline structure

## 📁 Project Structure

```
weather-etl-pipeline/
├── dags/
│   └── weather_etl_dag.py
├── output/
│   ├── raw_data.json
│   └── transformed_data.json
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Setup Instructions

1. Clone this repo:
   ```
   git clone https://github.com/your-username/weather-etl-pipeline.git
   cd weather-etl-pipeline
   ```

2. Create a virtual environment and install dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Start Airflow:
   ```
   airflow db init
   airflow users create ...
   airflow webserver -p 8080
   airflow scheduler
   ```

4. Open Airflow UI at `http://localhost:8080` and trigger the DAG.

## 📦 Output Example

```json
{
  "city": "Colombo",
  "temperature": 27.14,
  "humidity": 83,
  "weather": "broken clouds",
  "timestamp": "2025-04-19T22:21:31.392324"
}
```

## 🛠️ Technologies

- Python 3.10+
- Apache Airflow 2.7+
- OpenWeatherMap API

## 📄 License

MIT

![image](https://github.com/user-attachments/assets/faaba995-203c-4872-babe-08312149fba5)
![image](https://github.com/user-attachments/assets/62117f06-0811-4359-831a-d8f520ad794b)
![image](https://github.com/user-attachments/assets/5aded0af-c010-4103-93eb-b0859f98b185)
![image](https://github.com/user-attachments/assets/4e9ecbd1-c41a-49bd-a64f-6418cd05f432)
![image](https://github.com/user-attachments/assets/44a5fe8b-7d34-4968-95be-a1dcab1355cd)

