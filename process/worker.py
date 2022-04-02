#   -*- coding:utf-8 -*-
#   The worker.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:54 on 2022/4/2
from qtpandas.models.ProgressThread import ProgressWorker
import time
from utils.logger import Logger

class Worker(ProgressWorker):
    def __init__(self, name):
        super(Worker, self).__init__(name)
        self.log = Logger("fa").get_log()
        self.ans = None
        self.paras = None

    def get_ans(self):
        return self.ans

    def set_parameters(self,** kwargs):
        self.paras = kwargs

    def run(self):
        self.log.info("task starts at "+time.strftime("%H:%M:%S",time.localtime()))
        self.ans = self.handle_job(** self.paras)
        self.log.info("task finishs at " + time.strftime("%H:%M:%S", time.localtime()))

    def handle_job(self, ** kwargs):
        pass

    def set_job(self, func):
        self.handle_job = func