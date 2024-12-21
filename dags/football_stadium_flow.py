import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipelines.football_stadium_etl import extract_data, transform_data, load_data
default_args = {
    'owner': 'Hong Pham Van',
    'start_date': datetime(2024, 12, 22),
}

with DAG(
    dag_id= 'football_stadium_flow',
    default_args=default_args,
    schedule_interval= None,
    catchup=False,
) as dag:
    
    extract_wikipedia_data = PythonOperator(
        task_id = "extract_wikipedia_data",
        python_callable= extract_data,
        provide_context=True,
        op_kwargs={
            'url': r'https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity',
            'target_table_index': 2
        }
    )

    extract_wikipedia_data