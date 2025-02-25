import logging
import os

class CostumeLogger:
    @staticmethod
    def log():
        log_file_path = os.path.join(os.getcwd(), 'Logs', 'Test_session_logs.log')
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        logger = logging.getLogger()

        if logger.hasHandlers():
            logger.handlers.clear()

        if not logger.hasHandlers():
            fhandler = logging.FileHandler(filename=log_file_path, mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)

        return logger
