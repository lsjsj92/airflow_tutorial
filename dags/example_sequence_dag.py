
from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule

default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

dag_args = dict(
    dag_id="tutorial-dag-sequence",
    default_args=default_args,
    description='tutorial DAG sequence',
    schedule_interval=timedelta(minutes=50),
    start_date=datetime(2022, 2, 1),
    tags=['example-sj'],
)

def random_branch_path():
    # 필요 라이브러리는 여기서 import
    # https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#writing-a-dag 참고
    from random import randint

    return "path1" if randint(1, 2) == 1 else "my_name_en"

with DAG( **dag_args ) as dag:

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BranchPythonOperator(
        task_id='branch',
        python_callable=random_branch_path,
    )
    
    t3 = BashOperator(
        task_id='my_name_ko',
        depends_on_past=False,
        bash_command='echo "안녕하세요."',
    )

    t4 = BashOperator(
        task_id='my_name_en',
        depends_on_past=False,
        bash_command='echo "Hi"',
    )

    complete = BashOperator(
        task_id='complete',
        depends_on_past=False,
        bash_command='echo "complete~!"',
        trigger_rule=TriggerRule.NONE_FAILED
    )

    dummy_1 = DummyOperator(task_id="path1")


    t1 >> t2 >> dummy_1 >> t3 >> complete
    t1 >> t2 >> t4 >> complete
