from datetime import timedelta
from airflow import DAG
from airflow.operator.python import pythonOperator
from airflow.utils.dates import dats_ago
import logging

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@examples.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def scrape():
    logging.info("scrape scraping")


def process():
    logging.info("process scraping")


def save():
    loggging.info("save scraping")


with Dag(
        'first',
        default_args=default_args,
        description='A simple',
        schedule_interval=timedelta(days=1),
        start_date=days_ago(2),
        tags=['example'],
) as dag:
    scrape_task = pythonOperator(task_id="scrape", python_callable=screpa)
    process_task = pythonOperator(task_id="process", python_callable=process)
    save_task = pythonOperator(task_id="save", python_callavle=save)