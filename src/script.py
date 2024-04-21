import datetime

import pandas as pd
from sqlalchemy import create_engine
from uuid import uuid4

import os

from db_check import check_columns
from dotenv import load_dotenv

load_dotenv('../.env')


def convert_to_db(import_file: str, table_name: str):
    """
    Convert Excel file to SQL database.

    Parameters
    ----------
    import_file : str
        Path to Excel or CSV file.
    table_name: str
        Name of SQL table to insert.

    Returns
    -------
    """
    if import_file.endswith('.csv'):
        # read in csv file
        print("CSV file uploaded")
        df = pd.read_csv(import_file, encoding="cp1251", low_memory=False)
    elif import_file.endswith('.xls') or import_file.endswith('.xlsx'):
        # read in excel file
        print("Excel file uploaded")
        df = pd.read_excel(import_file)
    else:
        raise ValueError(f'Wrong file extension: {import_file}. Import CSV or XLS/XLSX file')
    df.insert(0, "sync_id", value=[uuid4() for _ in range(len(df))], allow_duplicates=False)
    # df['transaction_id'] = [str(uuid4()) for _ in range(len(df))]
    df.insert(1, "created_at", value=datetime.datetime.now(), allow_duplicates=False)
    print("DatFrame form Excel created!")
    print("Check columns of excel file and db table")
    check_columns(df=df, table_name=table_name)
    # convert to SQL database
    engine = create_engine(
        f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}')
    engine.connect()
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    print(f'{len(df)} lines successfully added to SQL table {table_name}')
