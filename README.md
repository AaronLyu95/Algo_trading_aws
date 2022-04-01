# ETL process


## Introduction
The ETL process will extract S&P 100 stock candles data from finnhub.io through its API, and 
load data to 2 tables in Amazon rds postgreSQL database. The two tables are
us_equity_1min_finn table and us_equity_daily_finn table. We can know the granularity of data from these two
tables are day-level and 1-minute-level by their names.


## Explanations
Run etl_one_time.sh file to initialize the database, and insert history data.
The etl_one_time.py must be followed by 4 arguments. The first 2 arguments are start time and 
end time for daily data table. The last 2 arguments are start time and end time for minute-level data table.

Using crontab to run etl_routine.sh file to update data to existing tables.

All utility functions are stored in utils.

Prepare your own pickle file, and the pickle preparation file is included in utils folder. You can\
filling with your own credentials.

## Files
### etl_one_time.py
Initialize tables from database, and load historical data to database.
Need 4 arguments which are (start time for daily table), (end time for daily table), (start time for 1min table), (end time for 1min table)

### etl_one_time.sh
Run etl_one_time.py on linux

### etl_routine.py
Run daily job for updating data from last time to current time for both tables.

### etl_routine.sh
Run etl_routine.py on linux

### .prepare_pickle_file.py
Provide a template to make your own pickle file.

### config.py
Basic configs include: database config, finnhub config, twilio_config, database tables config.

### db_utils.py
Provide database utilities.

### finnhub_utils.py
Provide finnhub utilities.

### twilio_utils.py
Provide twilio utilities.

### log_utils.py
Provide logging utilities to write log file.

### gmail_utils.py
Provide gmail send message utilities and making your own credential template.

### etl_utils.py
Main utilities for whole ETL process.

## us_equity_1min_finn.sql
Create intraday data table on database.

## us_equity_daily_finn.sql
Create daily data table on database.



## Automation
In order to automatically start ETL process every day, we use crontab in linux to run \
etl_routine.sh at 22:00EST by system itself. \
The contab command is 0 22 * * * bash /home/ubuntu/Algo_trading/ETL/etl_routine.sh




## Table visualization
### us_equity_1min_finn
![img_1min](https://drive.google.com/uc?export=view&id=16C2CocFRG_PL00dOVe0a7rPiuUqXP6Kt)



### us_equity_daily_finn
![img_daily](https://drive.google.com/uc?export=view&id=1Z6KgnSuieGsYTAHCfKGdqbzwmyLaOKub)

