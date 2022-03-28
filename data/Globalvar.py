#   -*- coding:utf-8 -*-
#   The Globalvar.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:54 on 2022/3/28
from utils.logger import  Logger
log = Logger('fa').get_log()
def init_():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value
    log.info("set value "+ name )
    log.info(_global_dict)


def get_value(name, defValue = None):
    log.info("get value "+ name )
    log.info(_global_dict)
    try:
        return _global_dict[name]
    except KeyError:
        log.error("no values matched key " + name )
        return defValue