import json
from pendulum import datetime
from datetime import timedelta

from airflow.decorators import (
    dag,
    task,
)  

from time import sleep

@dag(
    # This defines how often your DAG will run, or the schedule by which your DAG runs. In this case, this DAG
    # will run daily
    schedule=timedelta(minutes=1),
    # This DAG is set to run for the first time on January 1, 2023. Best practice is to use a static
    # start_date. Subsequent DAG runs are instantiated based on the schedule
    start_date=datetime(2023, 1, 1),
    # When catchup=False, your DAG will only run the latest run that would have been scheduled. In this case, this means
    # that tasks will not be run between January 1, 2023 and 30 mins ago. When turned on, this DAG's first
    # run will be for the next 30 mins, per the its schedule
    catchup=False,
    default_args={
        "retries": 2,  # If a task fails, it will retry 2 times.
    },
    tags=["example"],
)  # If set, this tag is shown in the DAG view of the Airflow UI
def minha_dag_hello_world():
    """
    ### Basic ETL Dag
    This is a simple ETL data pipeline example that demonstrates the use of
    the TaskFlow API using three simple tasks for extract, transform, and load.
    For more information on Airflow's TaskFlow API, reference documentation here:
    https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html
    """
    @task
    def minha_primeira_atividade():
        print("essa foi a primeira atividade")
        sleep(1)

    @task
    def minha_segunda_atividade():
        print("essa foi a segunda atividade")
        sleep(1)

    @task
    def minha_terceira_atividade():
        print("essa foi a terceira atividade")
        sleep(1)

    # Definindo as dependências
    t1 = minha_primeira_atividade()
    t2 = minha_segunda_atividade()
    t3 = minha_terceira_atividade()

    t1 >> t2 >> t3  # Isso define que t1 é predecessor de t2, e t2 é predecessor de t3

minha_dag_hello_world()