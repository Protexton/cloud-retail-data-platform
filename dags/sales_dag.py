from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

default_args = {
    'owner': 'iker',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

def extract():
    print("📦 Extracción de datos simulada completada.")

def transform():
    print("🔧 Transformación de datos (normalización, joins, cálculo de KPIs)")

def load():
    print("📥 Carga de datos enriquecidos en almacén (simulado)")

with DAG(
    dag_id='sales_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Pipeline ETL de ventas para retail',
    tags=['retail', 'ETL', 'ventas']
) as dag:

    t1 = PythonOperator(
        task_id='extract_data',
        python_callable=extract
    )

    t2 = PythonOperator(
        task_id='transform_data',
        python_callable=transform
    )

    t3 = PythonOperator(
        task_id='load_data',
        python_callable=load
    )

    t1 >> t2 >> t3
