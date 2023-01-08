# catchup을 사용한 데이터 백필
import pendulum
import datetime as dt
from airflow import DAG
from airflow.operators.python import PythonOperator

kr_tz = pendulum.timezone("Asia/Seoul")
dag = DAG(
    dag_id="08_no_catchup",
    schedule_interval="*/2 * * * *",
    start_date=dt.datetime(2023, 1, 6, 17, 45, tzinfo=kr_tz),
    end_date=dt.datetime(2023, 1, 6, 18, 5, tzinfo=kr_tz),
    catchup=False,
)


def _print_hello():
    print("Hello, It's work!")


print_hello = PythonOperator(
    task_id="print_hello", python_callable=_print_hello, dag=dag
)


print_hello
