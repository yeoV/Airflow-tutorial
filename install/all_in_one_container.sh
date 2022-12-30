# ! /bin/bash
docker run -it -p 8080:8080 \
-v /Users/lsy/workspace/DE/Airflow-tutorial/dags:/opt/airflow/dags \
--entrypoint /bin/bash \
--name airflow \
apache/airflow \
-c '( airflow db init && \
airflow users create \
--username admin \
--password admin \
--firstname Lee \
--lastname SY \
--role Admin \
--email test@naver.com); \
airflow webserver & airflow scheduler'
