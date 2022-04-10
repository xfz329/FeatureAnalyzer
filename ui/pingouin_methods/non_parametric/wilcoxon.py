#   -*- coding:utf-8 -*-
#   The wilcoxon.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 21:50 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Wilcoxon_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Wilcoxon signed-rank test")
        self.url = "https://pingouin-stats.org/generated/pingouin.wilcoxon.html#pingouin.wilcoxon"
        self.log.info("wilcoxon method!")

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
        paras = {}
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("x",self.df[x[0]])

        y = self.listView_2.model().stringList()
        if len(y) == 0:
            paras.setdefault("y", None)
        elif len(y) == 1:
            paras.setdefault("y", self.df[y[0]])
        else:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置为空或一个。", QMessageBox.Ok)
            return

        paras.setdefault("alternative", self.comboBox_p1.currentText())

        try:
            kwargs = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成dict类型，当前已重置为{}。", QMessageBox.Ok)
            kwargs = {}

        if type(kwargs) is not dict:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成dict类型，当前已重置为{}。", QMessageBox.Ok)
            kwargs = {}
        for key in kwargs:
            paras.setdefault(key, kwargs[key])
        self.task.set_worker(pg.wilcoxon, **paras)