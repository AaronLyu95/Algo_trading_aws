from utils.etl_utils import unix_ts_to_datetime
from utils import etl_utils
from utils import config
import time
from utils import twilio_utils
import utils.etl_utils
import sys





def etl_multi():
    for type in ['daily', 'intraday']:
        start = etl_utils.get_last_time(config.table_config[type])
        end = etl_utils.get_current_time()
        try:
            utils.etl_utils.etl_main(type, start, end)
        except Exception as error:
            error_message = f"Your {type} ETL process meets an error: {error}"
            twilio_utils.twilio_message(error_message)
        finally:
            final_message = f"Your {type} ETL process ended"
            # twilio_utils.twilio_message(final_message)




if __name__ == "__main__":
    start_time = etl_utils.get_current_time()
    message = f"Your ETL process begins at {start_time}"
    twilio_utils.twilio_message(message)
    etl_multi()
    end_time = etl_utils.get_current_time()
    cong_message = f"Congratulations! Your ETL process begins at {end_time}"
