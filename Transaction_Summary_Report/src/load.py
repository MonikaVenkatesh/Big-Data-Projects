import os
from sqlalchemy import create_engine

def load_to_target(df, db_conf, table_name):
    engine = create_engine(
        f"postgresql+psycopg2://{db_conf['user']}:{db_conf['password']}@{db_conf['host']}:{db_conf['port']}/{db_conf['database']}"
    )
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Loaded {table_name} into target DB")

def export_to_excel(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"📁 Exported: {output_path}")
