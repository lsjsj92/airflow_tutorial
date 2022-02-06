# airflow_tutorial

**airflow python tutorial & example**

해당 repo는 블로그에 기술해 놓은 내용에 사용된 airflow example 코드입니다.

**blog**
- https://lsjsj92.tistory.com/

----
## Dags dir
- example_basic_dag.py
    - Basic example DAG
    - Same as airflow doc : https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
    - Blog description : https://lsjsj92.tistory.com/631
- example_sequence_dag.py
    - Sequence DAG example ( dag branch )
- example_python_dag.py
    - Python basic DAG example
- example_ml_dag.py
    - Machine Learning basic DAG example
    - Run with MLproject dir
    - Titanic data & scikit-learn
- example_slack_dag.py
    - Airflow slack alert example
    - Basically the same as example_ml_dag.py code and added slack api

---- 

## Repository file structure

```

airflow_tutorial
│   README.md
│   .gitignore    
│
└───dags
│   │   example_basic_dag.py
│   │   example_sequence_dag.py
│   │   example_python_dag.py
│   │   example_ml_dag.py
│   │   example_slack_dag.py
└───MLproject
│   │   config.py
│   │   dataio.py
│   │   model.py
│   │   preprocess.py
│   │   titanic.py
│   └───data
│   └─────titanic
│   │     │   train.csv
│   │     │   prepro_titanic.csv
└───utils
│   │   slack_alert.py
```
