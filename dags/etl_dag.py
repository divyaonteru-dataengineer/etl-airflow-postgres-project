
from airflow import DAG
from datetime import datetime

dag = DAG(
    'etl_pipeline',
    start_date=datetime(2024,1,1)
)
