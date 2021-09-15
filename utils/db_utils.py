import pandas as pd
import psycopg2 as pg
from utils.config import db_config


def conn_engine():
    """
    Create a postgres db engine
    """
    engine = pg.connect(
        host=db_config['host'],
        port=db_config['port'],
        database="postgres",
        user=db_config['user'],
        password=db_config['passowrd']
    )
    return engine



def read_table(table_name):
    with conn_engine() as db:
        query = f'SELECT * from {table_name}'
        return pd.read_sql_query(query, db)


def exec_query(query):

    df = pd.DataFrame()
    with conn_engine() as db:
        df = pd.read_sql(query, db)
    return df
