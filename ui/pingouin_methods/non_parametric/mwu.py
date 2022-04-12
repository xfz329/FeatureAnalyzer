#   -*- coding:utf-8 -*-
#   The mwu.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 21:35 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Mwu_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Mann-Whitney U Test (= Wilcoxon rank-sum test)")
        self.url = "https://pingouin-stats.org/generated/pingouin.mwu.html#pingouin.mwu"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "mwu method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(2)
        self.label_l1.setText("x")
        self.label_l2.setText("y")

        self.show_choose_parameters(1)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")

        self.show_set_parameters(1)
        self.label_s1.setText("kwargs")
        self.lineEdit_s1.setText("{}")

    def start_analyse(self):
        self.paras.clear()
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("x",self.df[x[0]])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("y", self.df[y[0]])

        self.paras.setdefault("alternative", self.comboBox_p1.currentText())

        try:
            kwargs = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成dict类型，当前已重置为{}。", QMessageBox.Ok)
            kwargs = {}
        if type(kwargs) is not dict:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成dict类型，当前已重置为{}。", QMessageBox.Ok)
            kwargs = {}
        for key in kwargs:
            self.paras.setdefault(key, kwargs[key])

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.mwu, **self.paras)