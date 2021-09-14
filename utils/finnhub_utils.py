import finnhub
import pandas as pd
from utils.config import finnhub_config

def finnhub_conn():
    """
    Create a finnhub connection through finnhub API
    """
    try:
        finnhub_client = finnhub.Client(api_key=finnhub_config['api'])
    except Exception as error:
        print(error)
    finally:
        finnhub_client.close()

def get_sp500_symbols():
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    symbols = df[0]['Symbol'].values.tolist()
    return symbols





