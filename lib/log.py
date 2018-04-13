import logging
import sys

class Log():
    is_init = 0
    logger = logging.getLogger("AppName")
    @staticmethod
    def init():
        #print Log.is_init
        if Log.is_init == 0:
            #Log.logger = logging.getLogger("AppName")
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
            file_handler = logging.FileHandler("test.log")
            file_handler.setFormatter(formatter)
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.formatter = formatter
            Log.logger.addHandler(file_handler)
            Log.logger.addHandler(console_handler)
            Log.logger.setLevel(logging.DEBUG)
            Log.is_init = 1
        #print Log.is_init
        return Log

    @staticmethod
    def ss(str1):
        Log.logger.info(str1)

    @staticmethod
    def debug(str1):
        Log.logger.debug(str1)

    @staticmethod
    def info(str1):
        Log.logger.info(str1)

    @staticmethod
    def warn(str1):
        Log.logger.warn(str1)

    @staticmethod
    def error(str1):
        Log.logger.error(str1)

    @staticmethod
    def fatal(str1):
        Log.logger.fatal(str1)

    @staticmethod
    def critical(str1):
        Log.logger.critical(str1)
