# 특정 시간 간격에 대한 이벤트 처리
import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="04_query_with_dates",
    schedule_interval=dt.timedelta(2),
    start_date=dt.datetime(2023, 1, 3),
    end_date=dt.datetime(2023, 1, 7),
)


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
