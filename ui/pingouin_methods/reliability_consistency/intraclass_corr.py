#   -*- coding:utf-8 -*-
#   The intraclass_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 12:14 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Intraclass_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Intraclass correlation")
        self.url = "https://pingouin-stats.org/generated/pingouin.intraclass_corr.html#pingouin.intraclass_corr"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "intraclass_corr method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(3)
        self.label_l1.setText("targets")
        self.label_l2.setText("raters")
        self.label_l3.setText("ratings")

        self.show_choose_parameters(1)
        self.label_p1.setText("nan_policy")
        self.comboBox_p1.addItem("raise")
        self.comboBox_p2.addItem("omit")

        self.show_set_parameters(0)

    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)

        targets = self.listView_1.model().stringList()
        if len(targets) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量targets能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("targets",targets[0])

        raters = self.listView_2.model().stringList()
        if len(raters) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量raters能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("raters", raters[0])

        ratings = self.listView_3.model().stringList()
        if len(ratings) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量ratings能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("ratings", ratings[0])

        self.paras.setdefault("nan_policy",self.comboBox_p1.currentText())

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.intraclass_corr, **self.paras)