#   -*- coding:utf-8 -*-
#   The rm_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 18:01 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Rm_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Repeated measures correlation")
        self.url = "https://pingouin-stats.org/generated/pingouin.rm_corr.html#pingouin.rm_corr"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "rm_corr method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(3)
        self.label_l1.setText("x")
        self.label_l2.setText("y")
        self.label_l3.setText("subject")

        self.show_choose_parameters(0)

        self.show_set_parameters(0)

    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)

        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("x",x[0])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("y", y[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("subject", subject[0])

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.rm_corr, **self.paras)