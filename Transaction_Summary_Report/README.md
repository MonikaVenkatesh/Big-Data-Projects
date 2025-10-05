step 1: create virtual env:

python -m venv etl
etl\Scripts\activate  


requirements:

pandas
sqlalchemy
psycopg2-binary
pyyaml
openpyxl

or - pip install -r requirements.txt


Run the pipeline:

python /path/to/banking_etl_project/src/main.py >> /path/to/logs/etl_run.log 2>&1


