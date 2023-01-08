import datetime as dt
from airflow import DAG


dag = DAG(
    dag_id="02_with_end_date",
    schedule_interval=dt.timedelta(2),
    start_date=dt.datetime(2023, 1, 3),
    end_date=dt.datetime(2023, 1, 7),
)
