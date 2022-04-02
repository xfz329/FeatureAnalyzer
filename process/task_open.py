#   -*- coding:utf-8 -*-
#   The task_open.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 11:17 on 2022/4/2
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
from process.task import Task


class TaskOpen(Task):

    def __init__(self,func,work_name):
        Task.__init__(self,func,work_name)

    def set_worker(self):
        self.worker.set_job(self.open)
        file = self.get_file_to_open()
        self.worker.set_parameters(file = file)
        self.log.info("The work job has been bounded to " + str(self.worker.handle_job))
        self.thread.start()

    def get_file_to_open(self):
        f = QFileDialog.getOpenFileName(None, "打开", "D:\\UrgeData\\Desktop", ".csv *.*")
        file = f[0]
        if file == "":
            self.log.error("No files is selected to open")
            return None
        self.log.info("Open file " + file)
        return file

    def open(self,file):
        df = None
        if file is None:
            self.log.error("File name is empty ")
            return None
        if file.endswith(".csv"):
            df = pd.read_csv(file)
            self.log.info("open files finished!")
        elif file.endswith(".xls") or file.endswith(".xlsx"):
            df = pd.read_excel(file)
            self.log.info("open files finished!")
        else:
            self.log.error("Unsupported file type "+file)
        return df