#   -*- coding:utf-8 -*-
#   The compute_effsize.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 13:55 on 2022/4/10

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Compute_effsize_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Calculate effect size between two set of observations")
        self.url = "https://pingouin-stats.org/generated/pingouin.compute_effsize.html#pingouin.compute_effsize"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "compute_effsize method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(2)
        self.label_l1.setText("x")
        self.label_l2.setText("y")

        self.show_choose_parameters(2)
        self.label_p1.setText("paired")
        self.comboBox_p1.addItem("False")
        self.comboBox_p1.addItem("True")
        self.label_p2.setText("eftype")
        self.comboBox_p2.addItem("cohen")
        self.comboBox_p2.addItem("none")
        self.comboBox_p2.addItem("hedges")
        self.comboBox_p2.addItem("r")
        self.comboBox_p2.addItem("eta-square")
        self.comboBox_p2.addItem("AUC")
        self.comboBox_p2.addItem("CLES")


        self.show_set_parameters(0)

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

        self.paras.setdefault("paired",self.comboBox_p1.currentIndex()==1)
        self.paras.setdefault("eftype",self.comboBox_p2.currentText())

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.compute_effsize, **self.paras)