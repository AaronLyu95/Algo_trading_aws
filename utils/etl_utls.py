import pandas as pd

from utils.finnhub_utils import finnhub_conn
from utils.finnhub_utils import get_sp500_symbols









def unix_ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')



def datetime_to_unix_ts(datetime_input) -> int:
    """
    input:"2021-09-01 09:00:00AM"
    """
    return int(dateutil.parser.parse(datetime_input).timestamp())



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
            time.sleep(2)
            resp = finn.stock_candles(symbol, interval, start_unix, end_unix)
            resp = pd.DataFrame(resp)
            if resp['s'] == 'no_data':
                # drop no data column
                index = resp[resp['s'] == 'no_data'].index
                resp.drop(index, inplace=True)
            stock_data['symbol'] = symbol
            stock_data['tt'] = pd.to_datetime(stock_data['t'], unit='s', utc=True)
            stock_data = pd.concat(
                [pd.DataFrame(resp), stock_data],
                ignore_index=True,
            )
            end_unix = resp['t'][0] - 1

    return stock_data





def get_daily_data(start, end):
    daily_data = pd.DataFrame(
        columns=['c', 'h', 'l', 'o', 's', 't', 'v', 'symbol', 'tt'])
    sp500_symbols = get_sp500_symbols()
    for symbol in sp500_symbols:
        daily_stock = get_stock_candles(symbol, 'D', start, end)
        daily_data = pd.concat(
            [daily_stock, daily_data],
            ignore_index=True,
        )
    return daily_stock




def get_intraday_data(start, end):
    intraday_data= pd.DataFrame(
        columns=['c', 'h', 'l', 'o', 's', 't', 'v', 'symbol', 'tt'])
    sp500_symbols = get_sp500_symbols()
    for symbol in sp500_symbols:
        intraday_stock = get_stock_candles(symbol, '1', start, end)
        intraday_data = pd.concat(
            [intraday_stock, intraday_data],
            ignore_index=True,
        )
    return intraday_data



