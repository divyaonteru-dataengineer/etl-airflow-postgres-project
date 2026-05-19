
from airflow import DAG
from datetime import datetime

dag = DAG(
    'etl_pipeline',
    start_date=datetime(2026,05,19)
)
