import datetime as dt
from airflow import DAG

import pendulum
from airflow.operators.python import PythonOperator

# Korea Time Zone
kr_tz = pendulum.timezone("Asia/Seoul")

dag = DAG(
    dag_id="execution_time_test",
    schedule_interval="*/2 * * * *",
    start_date=dt.datetime(2023, 1, 4, 14, 20, tzinfo=kr_tz),
)


def _print_hello():
    print("Hello World")


print_hello = PythonOperator(
    task_id="print_hello", python_callable=_print_hello, dag=dag
)


print_hello
