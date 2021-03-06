#   -*- coding:utf-8 -*-
#   The multivariate_normality.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:47 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Multivariate_normality_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Henze-Zirkler multivariate normality test")
        self.url = "https://pingouin-stats.org/generated/pingouin.multivariate_normality.html#pingouin.multivariate_normality"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "multivariate_normality method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(1)
        self.label_l1.setText("X")

        self.show_choose_parameters(0)

        self.show_set_parameters(1)
        self.label_s1.setText("alpha")
        self.lineEdit_s1.setText("0.05")

    def start_analyse(self):
        self.paras.clear()

        x = self.listView_1.model().stringList()
        self.paras.setdefault("X",self.df[x])

        try:
            alpha =float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置成float类型。当前已被重置为0.05", QMessageBox.Ok)
            alpha = 0.05
        if type(alpha) is float:
            if alpha<0 or alpha>1:
                QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置在[0,1]。当前已被重置为0.05", QMessageBox.Ok)
                alpha = 0.05
        else:
            alpha =0.05
        self.paras.setdefault("alpha",alpha)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.multivariate_normality, **self.paras)