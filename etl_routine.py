from utils.etl_utils import unix_ts_to_datetime
from utils import etl_utils
from utils import config
import time
from utils import twilio_utils
import utils.etl_utils
import sys
from utils.gmail_utils import send_message_gmail
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.log_utils import etl_log





def etl_multi(type):
    start = etl_utils.get_last_time(config.table_config[type])
    end = etl_utils.get_current_time()
    try:
        start_t = etl_utils.get_current_time()
        utils.etl_utils.etl_main(type, start, end)
        end_t = etl_utils.get_current_time()
    except Exception as error:
        error_message = f"Your {type} ETL process occurs an error: {error}"
        send_message_gmail(f"{type} ETL error", error_message)
        etl_log(error_message, 'ERROR')
        twilio_utils.twilio_message(error_message)
    finally:
        final_message = f"Your {type} ETL process begun at {start_t} and successfully finished at {end_t}"
        send_message_gmail(f"{type} ETL", final_message)
        etl_log(final_message, 'INFO')
        twilio_utils.twilio_message(final_message)


def etl_multi_thread():

    '''
    Since most of our ETL jobs are I/O work, I use ThreadPoolExecuter instead of multi_processing to write data to
    database from 2 threads.
    '''

    types = ['daily', 'intraday']
    try:
        with ThreadPoolExecutor(max_workers=2) as executor:
            etl_tasks = [executor.submit(etl_multi, type) for type in types]
            for task in as_completed(etl_tasks):
                print(task.result())
    except Exception as error:
        thread_error_message = f"Your multi thread tasks occurs and error: {error}"
        send_message_gmail(f"ETL multi thread error", thread_error_message)






if __name__ == "__main__":
    start_time = etl_utils.get_current_time()
    message = f"Your ETL process begins at {start_time}"
    send_message_gmail('ETL begins', message)
    # twilio_utils.twilio_message(message)
    etl_multi_thread()
    end_time = etl_utils.get_current_time()
    cong_message = f"Congratulations! Your today ETL process successfully finished at {end_time}"
    send_message_gmail('ETL ends', cong_message)
    etl_log(cong_message, 'INFO')
    # twilio_utils.twilio_message(cong_message)

