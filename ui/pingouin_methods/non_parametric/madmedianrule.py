#   -*- coding:utf-8 -*-
#   The madmedianrule.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 21:30 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Madmedianrule_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Robust outlier detection based on the MAD-median rule")
        self.url = "https://pingouin-stats.org/generated/pingouin.madmedianrule.html#pingouin.madmedianrule"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "madmedianrule method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(1)
        self.label_l1.setText("a")

        self.show_choose_parameters(0)

        self.show_set_parameters(0)

    def start_analyse(self):
        self.paras.clear()

        a = self.listView_1.model().stringList()
        if len(a) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("a",self.df[a[0]])

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.madmedianrule, **self.paras)