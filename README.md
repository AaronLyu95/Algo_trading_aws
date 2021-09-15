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


## Table visualization
### us_equity_1min_finn
![img_1min](https://drive.google.com/uc?export=view&id=1MzMQc_D33CiufKDnTBfCD8kfT3awZRS5)



### us_equity_daily_finn
![img_daily](https://drive.google.com/uc?export=view&id=1MzMQc_D33CiufKDnTBfCD8kfT3awZRS5)

