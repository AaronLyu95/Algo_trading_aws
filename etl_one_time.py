from utils.etl_utils import unix_ts_to_datetime
from utils import etl_utils
import time
from utils import twilio_utils
from utils.db_utils import conn_engine
import utils.etl_utils
import sys
import os
import traceback
from utils.gmail_utils import send_message_gmail
from utils.log_utils import etl_log


def etl_first(type, start, end):
    try:
        utils.etl_utils.etl_main(type, start, end)
    except Exception as error:
        error_message = f"Your {type} ETL process meets an error: {error}"
        print(error_message)
        print(traceback.format_exc())
        etl_log(error_message, 'ERROR')
        # twilio_utils.twilio_message(error_message)
    finally:
        final_message = f"Your {type} ETL process ended"
        etl_log(final_message, 'INFO')
        # twilio_utils.twilio_message(final_message)








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
    message = f"Your initial ETL process begins at {start_time}"
    send_message_gmail('Initial ETL begins', message)
    etl_log(message, 'INFO')
    # twilio_utils.twilio_message(message)
    etl_first('daily', sys.argv[1], sys.argv[2])
    etl_first('intraday', sys.argv[3], sys.argv[4])
    end_time = etl_utils.get_current_time()
    cong_message = f"Congratulations! Your initial ETL process successfully finished at {end_time}"
    send_message_gmail('Initial ETL ends', cong_message)
    etl_log(cong_message, 'INFO')
    # twilio_utils.twilio_message(cong_message)

