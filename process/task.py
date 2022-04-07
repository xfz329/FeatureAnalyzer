#   -*- coding:utf-8 -*-
#   The task.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 11:13 on 2022/4/2
from qtpandas.models.ProgressThread import createThread
import pandas as pd
from process.worker import Worker
from utils.logger import Logger


class Task:

    def __init__(self,func,worker_name):
        self.worker = Worker(worker_name)
        self.thread = createThread(None, self.worker)
        self.worker.finished.connect(func)
        self.log = Logger("fa").get_log()

    def get_ans(self):
        return self.worker.get_ans()

    def set_worker(self,func,* pwargs, ** kwargs):
        self.worker.set_job(func)
        self.worker.set_parameters(* pwargs,**kwargs)
        self.log.info("The work job has been bounded to " + str(self.worker.handle_job))
        self.log.info("show pwargs")
        for l in pwargs:
            self.log.info(type(l))
            self.log.info(l)
            # if tp is not pd.core.frame.DataFrame:
            #     self.log.info("value is " + str(l)+" , type is "+str(tp))
            # else:
            #     self.log.info(" is a DataFrame")
        self.log.info("show kwargs")
        for key in kwargs.keys():
            self.log.info(type(key))
            if key != "data":
                self.log.info("key is "+key+" , value is "+str(kwargs[key]))
        self.thread.start()