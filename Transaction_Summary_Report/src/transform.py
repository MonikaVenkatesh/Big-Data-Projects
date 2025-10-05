import pandas as pd

def transform(df, report_name):
    if report_name == 'daily_summary':
        df['net_balance'] = df['total_credit'] - df['total_debit']

    elif report_name == 'inactive_accounts':
        df['days_inactive'] = (pd.Timestamp.now().normalize() - df['last_txn_date']).dt.days

    elif report_name == 'high_value_txn':
        df['flag'] = df['amount'].apply(lambda x: 'HIGH' if x > 200000 else 'NORMAL')

    return df
