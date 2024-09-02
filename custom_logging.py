import logging
import threading


class Logging:
    __instance = None
    __lock = threading.Lock()
        
    def __new__(cls, logger_name="my_logger", file_name="logs.log"):
        """
        Thread-safe singleton implementation of the Logging class.
        """
        if cls.__instance is None:
            cls.__lock.acquire()
            try:
                if cls.__instance is None:
                    cls.__instance = cls.get_logger(logger_name, file_name)
            finally:
                cls.__lock.release()
        
        return cls.__instance
    
    @staticmethod
    def get_logger(logger_name, file_name):
        """
        Return a logger object with the given name.

        If the logger doesn't exist yet, create it and configure it to log
        to the console with the format '%(asctime)s - %(name)s - %(levelname)s - %(message)s'.
        """
        logger=logging.getLogger(logger_name)
        if not logger.hasHandlers():
            logger.setLevel(logging.DEBUG)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

            # File Handler
            file_handler = logging.FileHandler(file_name)
            file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
        
        return logger

logger = Logging()