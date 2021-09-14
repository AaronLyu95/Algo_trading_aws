import psycopg2 as pg
from utils.config import db_config

def conn_engine():
    """
    Create a postgres db engine
    """
    engine = pg.connect(
        host = db_config['host'],
        port = db_config['port'],
        database = db_config['dbidentifier'],
        userr = db_config['user'],
        password = db_config['passowrd']
    try:
        yield engine
    except Exception as error:
        engine.rollback()
        print(error)
    else:
        engine.commit()
    finally:
        engine.close()
    )



def read_table(table_name, config_file='config.ini'):
    with connection(**config(config_file)) as db:
        query = f'SELECT * from {table_name}'
        return pd.read_sql_query(query, db)




def exec_query(query, config_file='config.ini'):
    df = pd.DataFrame()
    with connection(**config(config_file)) as db:
        df = pd.read_sql_query(query,db)
    return df

