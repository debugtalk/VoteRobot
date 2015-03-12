#encoding=utf-8

import logging, logging.config
from loggingConf import LOGGING_MyConfig

logging.config.dictConfig(LOGGING_MyConfig)
logger = logging.getLogger(__name__)
#logger.debug('A debug message')
