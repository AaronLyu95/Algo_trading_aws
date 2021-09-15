from utils.etl_utils import unix_ts_to_datetime
from utils import etl_utils
import time
from utils import twilio_utils
from utils.db_utils import conn_engine
import utils.etl_utils
import sys
import os



def etl_first(type, start, end):
    try:
        utils.etl_utils.etl_main(type, start, end)
    except Exception as error:
        error_message = f"Your {type} ETL process meets an error: {error}"
        print(error_message)
        twilio_utils.twilio_message(error_message)
    finally:
        final_message = f"Your {type} ETL process ended"
        twilio_utils.twilio_message(final_message)








if __name__ == "__main__":
    # run 2 sql files to create tables
    cur_path = os.path.dirname(os.path.realpath(__file__))
    us_equity_1min_finn = os.path.join(cur_path, 'data_sql', 'us_equity_1min_finn.sql')
    us_equity_daily_finn = os.path.join(cur_path, 'data_sql', 'us_equity_daily_finn.sql')
    with conn_engine() as db:
        with db.cursor() as cursor:
            with open(us_equity_1min_finn, 'r') as f:
                cursor.execute(f.read())
            with open(us_equity_daily_finn, 'r') as f:
                cursor.execute(f.read())
    #
    start_time = etl_utils.get_current_time()
    message = f"Your ETL process begins at {start_time}"
    twilio_utils.twilio_message(message)
    etl_first('daily', sys.argv[1], sys.argv[2])
    etl_first('intraday', sys.argv[3], sys.argv[4])
    end_time = etl_utils.get_current_time()
    cong_message = f"Congratulations! Your ETL process begins at {end_time}"

