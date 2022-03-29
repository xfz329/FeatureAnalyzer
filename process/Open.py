#   -*- coding:utf-8 -*-
#   The Open.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:29 on 2022/3/29
from PyQt5.QtWidgets import QFileDialog
from utils.logger import Logger
import pandas as pd

class OpenFiles:

    def __init__(self):
        self.log = Logger("fa").get_log()

    def open(self):
        f = QFileDialog.getOpenFileName(None,"打开","D:\\UrgeData\\Desktop",".csv *.*")
        file = f[0]
        if file == "":
            self.log.error("No files is selected to open")
            return None
        self.log.info("Open file "+file)
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xls") or file.endswith(".xlsx"):
            df = pd.read_excel(file)
        else:
            self.log.error("Unsupported file type "+file)
        return df