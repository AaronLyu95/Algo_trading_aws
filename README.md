# Algo_trading_aws

Run etl_one_time.sh file to initialize the database, and insert history data.
The etl_one_time.py must be followed by 4 arguments. The first 2 arguments are start time and end time for daily \
data table. The last 2 arguments are start time and end time for minute-lelvel data table.

Using crontab to run etl_routine.sh file to update data to existing tables.

All utility functions are stored in utils.

Prepare your own pickle file, and the prepare pickle file is included in utils folder.
