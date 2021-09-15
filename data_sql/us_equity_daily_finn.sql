
DROP TABLE IF EXISTS public.us_equity_daily_finn;

CREATE TABLE IF NOT EXISTS public.us_equity_daily_finn(
    close_price     numeric(9,3) ,
    high_price      numeric(9,3),
    low_price       numeric(9,3),
    open_price      numeric(9,3),
    status          varchar(5),
    time_stamp_unix bigint,
    volume          integer,
    time_stamp_nyc  timestamp,
    security_symbol varchar(7)
);