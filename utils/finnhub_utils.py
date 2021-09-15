import finnhub
import pandas as pd
from utils.config import finnhub_config
import datetime
import dateutil



def unix_ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def datetime_to_unix_ts(datetime_input) -> int:
    """
    input:"2021-09-01 09:00:00AM"
    """
    return int(dateutil.parser.parse(datetime_input).timestamp())




def finnhub_conn():
    """
    Create a finnhub connection through finnhub API
    """
    try:
        finn= finnhub.Client(api_key=finnhub_config['api'])
    except Exception as error:
        print(error)
    finally:
        return finn

def get_sp500_symbols():
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    symbols = df[0]['Symbol'].values.tolist()
    return symbols


def get_sp100_symbols():
    df = pd.read_html('https://en.wikipedia.org/wiki/S%26P_100')
    symbols = df[2]['Symbol'].values.tolist()
    return symbols




if __name__ == "__main__":
    with finnhub_conn() as finn:
        print(finn.stock_candles('AAPL','D',
                                 datetime_to_unix_ts("2021-08-30 00:00:00AM"),
                                 datetime_to_unix_ts("2021-09-13 11:59:59PM")))

