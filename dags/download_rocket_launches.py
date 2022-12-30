import json
import pathlib

import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


dag = DAG(
    dag_id="download_rocket_launchers",  # DAG 이름
    start_date=airflow.utils.dates.days_ago(14),  # workflow가 처음 실행되는 시간
    schedule_interval=None,  # 수동
)

download_launchers = BashOperator(
    task_id="download_launches",  # Task 이름
    bash_command="curl -o /tmp/launches.json \
        -L 'http://ll.thespacedevs.com/2.0.0/launch/upcoming'",
    dag=dag,  # DAG 변수에 대한 참조
)


def _get_pictures():
    # 경로 존재 확인
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)

    # launch.json 에 있는 모든 그림 파일 다운로드
    with open("/tmp/launches.json") as f:
        launches = json.load(f)
        image_urls = [launch["image"] for launch in launches["results"]]

        for image_url in image_urls:
            try:
                response = requests.get(image_url)
                image_filename = image_url.split("/")[-1]
                target_file = f"/tmp/images/{image_filename}"
                with open(target_file, "wb") as f:
                    f.write(response.content)
                print(f"Download {image_url} to {target_file}")
            except requests_exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL.")
            except requests_exceptions.ConnectionError:
                print(f"Could not connect to {image_url}")


get_pictures = PythonOperator(
    task_id="get_pictures", python_callable=_get_pictures, dag=dag
)

notify = BashOperator(
    task_id="notify",
    bash_command='echo "There are now $(ls /tmp/images. | wc -l) images."',
    dag=dag,
)

download_launchers >> get_pictures >> notify
