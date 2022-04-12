#   -*- coding:utf-8 -*-
#   The friedman.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:47 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Friedman_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Friedman test for repeated measurements")
        self.url = "https://pingouin-stats.org/generated/pingouin.friedman.html#pingouin.friedman"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "friedman method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(3)
        self.label_l1.setText("dv")
        self.label_l2.setText("within")
        self.label_l3.setText("subject")

        self.show_choose_parameters(1)
        self.label_p1.setText("method")
        self.comboBox_p1.addItem("chisq")
        self.comboBox_p1.addItem("f")


        self.show_set_parameters(0)

    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)

        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("dv",dv[0])

        within = self.listView_2.model().stringList()
        if len(within) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量within能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("within", within[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("subject", subject[0])
        self.paras.setdefault("method",self.comboBox_p1.currentText())

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.friedman, **self.paras)