# 특정 시간 간격에 대한 이벤트 처리
import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG()


fetch_events = BashOperator(
    task_id="04_query_with_dates",
    bash_command=(
        "mkdir -p /date && "
        "curl -o /data/events.json "
        "http://localhost:5000/events?"
        "start_date=2023-01-01&"
        "end_date=2023-01-03"
    ),
    dag=dag,
)
