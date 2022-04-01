#   -*- coding:utf-8 -*-
#   The task_open.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:19 on 2022/4/1
from PyQt5.QtWidgets import QFileDialog
from qtpandas.models.ProgressThread import ProgressWorker, createThread
import pandas as pd
from utils.logger import Logger

class OpenWorker(ProgressWorker):
    def __init__(self, name):
        super(OpenWorker, self).__init__(name)
        self.log = Logger("fa").get_log()
        self.df = None
        self.file = ""

    def getDataFrame(self):
        return self.df

    def open(self):
        f = QFileDialog.getOpenFileName(None, "打开", "D:\\UrgeData\\Desktop", ".csv *.*")
        self.file = f[0]
        if self.file == "":
            self.log.error("No files is selected to open")
            return None
        self.log.info("Open file " + self.file)

    def run(self):
        if self.file.endswith(".csv"):
            self.df = pd.read_csv(self.file)
            self.log.info("open files finished!")
        elif self.file.endswith(".xls") or self.file.endswith(".xlsx"):
            self.df = pd.read_excel(self.file)
            self.log.info("open files finished!")
        else:
            self.log.error("Unsupported file type "+self.file)

class TaskOpen:

    def __init__(self,func):
        self.worker = OpenWorker("open")
        self.thread = createThread(None, self.worker)
        self.worker.finished.connect(func)
        self.log = Logger("fa").get_log()

    def open_file(self):
        self.worker.open()
        self.thread.start()

    def getDataFrame(self):
        return self.worker.getDataFrame()