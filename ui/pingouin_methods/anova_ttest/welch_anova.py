#   -*- coding:utf-8 -*-
#   The welch_anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:11 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Welch_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("One-way Welch ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.welch_anova.html#pingouin.welch_anova"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "welch_anova method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(2)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("between变量")

        self.show_choose_parameters(0)
        self.show_set_parameters(0)


    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "独立变量能且只能设置一个。",QMessageBox.Ok)
            return
        self.paras.setdefault("dv",dv[0])
        between = self.listView_2.model().stringList()
        if len(between) != 1:
            QMessageBox.warning(None, "参数设置错误", "between变量能且只能设置一个。",QMessageBox.Ok)
            return
        self.paras.setdefault("between",between[0])

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.welch_anova, **self.paras)