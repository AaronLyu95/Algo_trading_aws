import logging
import os

def log_main(log_content, level, file_name):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    file = os.path.join(cur_path, '..', 'log', file_name)

    logger = logging.getLogger(file)
    logging.basicConfig(level=logging.DEBUG, filename=file, filemode='a',
                        format='%(asctime)s -%(filename)s -%(funcName)s -%(levelname)s - %(message)s')

    # Set handler and format

    if level == 'DEBUG':
        logger.debug(log_content)
    elif level == 'INFO':
        logger.info(log_content)
    elif level == 'WARNING':
        logger.warning(log_content)
    elif level == 'ERROR':
        logger.error(log_content)
    elif level == 'CRITICAL':
        logger.critical(log_content)



def etl_log(log_content, level):
    return log_main(log_content, level, 'etl_log.log')



if __name__ == "__main__":
    etl_log('t1', 'INFO')
    etl_log('t2', 'INFO')

