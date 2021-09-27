import pandas as pd
import time
from utils.config import table_config
from utils.finnhub_utils import finnhub_conn
from utils.finnhub_utils import get_sp100_symbols, get_sp500_symbols, sg_symbols
from utils.db_utils import exec_query
from utils.db_utils import conn_engine
from utils.finnhub_utils import unix_ts_to_datetime, datetime_to_unix_ts

import datetime
import dateutil
from io import StringIO


def get_last_time(table_name):
    last_time = exec_query(f"SELECT MAX(time_stamp_unix) FROM {table_name}")
    last_time = unix_ts_to_datetime(int(last_time.iloc[0, 0]))
    return last_time


def get_current_time():
    current_time = unix_ts_to_datetime(time.time())
    return current_time


def get_stock_candles(symbol, interval, start, end):
    """Return a dataframe from start to end on the stock

    Use previous timestamp +1 as next start timestamp
    """
    start_unix = int(dateutil.parser.parse(start).timestamp())
    end_unix = int(dateutil.parser.parse(end).timestamp())

    stock_data = pd.DataFrame(
        columns=['c', 'h', 'l', 'o', 's', 't', 'v']
    )
    with finnhub_conn() as finn:
        while start_unix < end_unix:
            time.sleep(2.1)
            resp = finn.stock_candles(symbol, interval, start_unix, end_unix)
            if resp['s'] == 'no_data':
                break
            resp = pd.DataFrame(resp)
            resp['tt'] = pd.to_datetime(resp['t'], unit='s', utc=True)
            resp['symbol'] = symbol
            resp['v'] = resp['v'].astype('int64')
            stock_data = pd.concat(
                [pd.DataFrame(resp), stock_data],
                ignore_index=True,
            )
            end_unix = resp['t'].min() - 1

    return stock_data


def get_daily_data(start, end):
    daily_data = pd.DataFrame(
        columns=['c', 'h', 'l', 'o', 's', 't', 'v', 'tt', 'symbol'])
    stock_symbols = sg_symbols()
    for symbol in stock_symbols:
        daily_stock = get_stock_candles(symbol, 'D', start, end)
        daily_data = pd.concat(
            [daily_stock, daily_data],
            ignore_index=True,
        )
    return daily_data


def get_intraday_data(start, end):
    intraday_data = pd.DataFrame(
        columns=['c', 'h', 'l', 'o', 's', 't', 'v', 'tt', 'symbol'])
    stock_symbols = sg_symbols()
    for symbol in stock_symbols:
        intraday_stock = get_stock_candles(symbol, '1', start, end)
        intraday_data = pd.concat(
            [intraday_stock, intraday_data],
            ignore_index=True,
        )
    return intraday_data


def etl_main(type, start, end):
    '''

    :param type: " 'daily' or 'intraday'"
    :param start: datetime
    :param end: datetime
    :return:
    '''
    if type == 'daily':
        df = get_daily_data(start, end)
    elif type == 'intraday':
        df = get_intraday_data(start, end)
    buffer = StringIO()
    df.to_csv(buffer,
              index_label=['open_price', 'close_price', 'low_price', 'high_price', 'status',
                           'time_stamp_unix', 'volume', 'time_stamp_nyc', 'security_symbol'],
              header=False,
              index=False)
    buffer.seek(0)
    with conn_engine() as db:
        with db.cursor() as cursor:
            cursor.copy_from(buffer, table=table_config[type], sep=",",
                             columns=('open_price', 'close_price', 'low_price', 'high_price', 'status',
                                      'time_stamp_unix', 'volume', 'time_stamp_nyc', 'security_symbol'))
