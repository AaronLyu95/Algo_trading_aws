import pickle
from configparser import ConfigParser
import os

cur_path = os.path.dirname(os.path.realpath(__file__))

ini_file = 'config.ini'
parser = ConfigParser()
parser.read(os.path.join(cur_path, ini_file))

credential_file = os.path.join(cur_path, parser['algo_db_rds']['credential'])

with open(credential_file, 'rb') as file:
    credentials = pickle.load(file)

# print(credentials)

db_config = {
    'host': parser['algo_db_rds']['host'],
    'port': int(parser['algo_db_rds']['port']),
    'dbname': parser['algo_db_rds']['dbname'],
    'dbidentifier': parser['algo_db_rds']['dbidentifier'],
    'user': parser['algo_db_rds']['user'],
    'passowrd': credentials['db']['password']
}

finnhub_config = credentials['finnhub']

twilio_config = credentials['twilio']

table_config = {
    'daily': 'us_equity_daily_finn',
    'intraday': 'us_equity_1min_finn'
}
