import pandas as pd
from sqlalchemy import create_engine
import yaml

def load_db_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def get_engine(db_conf):
    return create_engine(
        f"postgresql+psycopg2://{db_conf['user']}:{db_conf['password']}@{db_conf['host']}:{db_conf['port']}/{db_conf['database']}"
    )

def extract_data(db_conf, query_path):
    with open(query_path, 'r') as f:
        query = f.read()
    engine = get_engine(db_conf)
    df = pd.read_sql(query, engine)
    return df
