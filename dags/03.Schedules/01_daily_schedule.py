import datetime as dt
from airflow import DAG

dag = DAG(
    dag_id="01_daily_schedule",
    schedule_interval="@daily",
    start_date=dt.datetime(2023, 1, 3),
)
