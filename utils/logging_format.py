import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler
import os


class LoggingFormat:

    def get_logging_format(self, logger_name: str, env_variable_name =  'ENV_ALERDF_ERROR_LOG_FILE_PATH' ):
        logging_client = google.cloud.logging.Client()
        cloud_handler = CloudLoggingHandler(logging_client)

        logging.basicConfig(format='%(asctime)s %(funcName)s %(levelname)s: %(message)s', level=logging.INFO)

        file_handler = logging.FileHandler(os.getenv(env_variable_name))
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(funcName)s %(levelname)s: %(message)s'))

        logger = logging.getLogger(logger_name)
        logger.addHandler(file_handler)
        logger.addHandler(cloud_handler)

        return logger
