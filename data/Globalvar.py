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
    log.debug("set value "+ name + " to value " +str(value))
    log.debug(_global_dict)


def get_value(name, defValue = None):
    log.debug("get value "+ name )
    log.debug(_global_dict)
    try:
        return _global_dict[name]
    except KeyError:
        log.error("no values matched key " + name )
        return defValue

def delete_value(name):
    log.debug("delete value " + name)
    try:
        del _global_dict[name]
        log.debug(_global_dict)
    except KeyError:
        log.error("no values matched key " + name)

def get_dict():
    return _global_dict