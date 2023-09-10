"""
Description: DAG Script to execute the tasks.
"""

import datetime as dt
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from extract import extract
from transform import transform
from load import load



default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2023, 8, 29),
    'concurrency': 1,
    'retries': 0,
}
with DAG('etl_pipeline',
         default_args=default_args,
         catchup=False,
         schedule_interval='@daily',
         ) as dag:


    extract = PythonOperator(task_id='extract',
                              python_callable=extract,
                              dag=dag)
    transform = PythonOperator(task_id='transform',
                                python_callable=transform,
                                dag=dag
                                )
    load = PythonOperator(task_id='load',
                           python_callable=load,
                           dag=dag,
                           )

    extract >> transform >> load
   
