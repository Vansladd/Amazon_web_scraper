from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
from etl import run_etl


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="web_scraping_etl_pipeline",
    default_args=default_args,
    description="Web Scraping ETL Pipeline",
    schedule_interval="0 12 * * *",
    start_date=datetime(2025,4,5),
    catchup=False,
    tags=['web_scraping', 'ETL'],
    ) as dag :

    etl_task = PythonOperator(
        task_id = "run_etl",
        python_callable=run_etl,
    )