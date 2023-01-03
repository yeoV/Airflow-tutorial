# 실행 날짜에 따른 데이터 파티셔닝
import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG()


fetch_events = BashOperator(
    task_id="04_query_with_dates",
    bash_command=(
        "mkdir -p /date && "
        "curl -o /data/events/{{ds}}.json "  # 파일명에 ds 값을 통한 파티셔닝
        "http://localhost:5000/events?"
        "start_date={{ds}}&"  # Jinja template 으로 execution_date 삽입
        "end_date={{next_ds}}"
    ),
    dag=dag,
)
