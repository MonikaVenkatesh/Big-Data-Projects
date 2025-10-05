import os
from datetime import datetime
from src.extract import load_db_config, extract_data
from src.transform import transform
from src.load import load_to_target, export_to_excel

def run_pipeline():
    config = load_db_config('config/db_config.yaml')
    query_dir = 'config/queries'
    output_dir = 'output/reports'

    reports = {
        'daily_summary': os.path.join(query_dir, 'daily_summary.sql'),
        'inactive_accounts': os.path.join(query_dir, 'inactive_accounts.sql'),
        'high_value_txn': os.path.join(query_dir, 'high_value_txn.sql'),
    }

    for name, path in reports.items():
        print(f"\n🔹 Running pipeline for {name}")
        df = extract_data(config['source_db'], path)
        df = transform(df, name)
        load_to_target(df, config['target_db'], name)
        export_to_excel(df, os.path.join(output_dir, f"{name}_{datetime.now().strftime('%Y%m%d')}.xlsx"))

if __name__ == '__main__':
    run_pipeline()
