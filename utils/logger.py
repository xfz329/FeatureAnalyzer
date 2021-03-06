import logging
import logging.config
from pathlib import Path
import os, sys

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

LOG_PATH = os.path.join(BASE_DIR,'log')
print(LOG_PATH)
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
DEBUG_FILE = os.path.join(LOG_PATH,'debug.log')
WARN_FILE = os.path.join(LOG_PATH,'warn.log')
INFO_FILE = os.path.join(LOG_PATH,'info.log')
FILES = [DEBUG_FILE, WARN_FILE, INFO_FILE]

for f in FILES:
    if not os.path.exists(f):
        if str(sys.platform).startswith('win'):
            with open(f, 'a+') as fp:
                fp.close()
        else:
            os.mknod(f)


config= {
    'version' : 1,
    'disable_existing_loggers' : False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters' : {
    },
    'handlers': {
        'console' : {
            'level' : 'INFO',
            'class' : 'logging.StreamHandler',
            'formatter' : 'simple',
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/debug.log'),
            'formatter' : 'verbose',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 10,  # 备份数
            'encoding': 'utf-8',  # 设置默认编码
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/info.log'),
            'formatter' : 'verbose',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,  # 备份数
            'encoding': 'utf-8',  # 设置默认编码
        },
        'warn': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/warn.log'),
            'formatter' : 'verbose',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,  # 备份数
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    'loggers' : {
        'fa' : {
            'handlers' : ['console', 'debug','info','warn'],
            'level' : 'DEBUG',
        }
    }
}
class Logger:
    def __init__(self,logger_name):
        logging.config.dictConfig(config)
        self.__logger=logging.getLogger(logger_name)

    def get_log(self):
        return self.__logger

if __name__ == "__main__":
    t=Logger('fa')
    t.get_log().debug("debug")
    t.get_log().info("info")
    t.get_log().warning("warning")
    t.get_log().error("error")