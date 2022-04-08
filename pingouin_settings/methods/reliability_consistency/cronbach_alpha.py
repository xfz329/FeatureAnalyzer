#   -*- coding:utf-8 -*-
#   The cronbach_alpha.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 12:14 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Cronbach_alpha_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Cronbach’s alpha reliability measure")
        self.url = "https://pingouin-stats.org/generated/pingouin.cronbach_alpha.html#pingouin.cronbach_alpha"
        self.log.info("cronbach_alpha method!")

        self.show_add_parameter(3)
        self.label_l1.setText("items")
        self.label_l2.setText("scores")
        self.label_l3.setText("subject")

        self.show_choose_parameters(1)
        self.label_p1.setText("nan_policy")
        self.comboBox_p1.addItem("pairwise")
        self.comboBox_p2.addItem("listwise")

        self.show_set_parameters(1)
        self.label_s1.setText("ci")
        self.lineEdit_s1.setText("0.95")

    def start_analyse(self):
        lparas =()
        paras = {}
        paras.setdefault("data",self.df)

        items = self.listView_1.model().stringList()
        if len(items) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量items能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("items",items[0])

        scores = self.listView_2.model().stringList()
        if len(scores) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量scores能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("scores", scores[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])

        paras.setdefault("nan_policy",self.comboBox_p1.currentText())

        try:
            ci =float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "变量ci必须设置成float类型。当前已被重置为0.95", QMessageBox.Ok)
            ci = 0.95
        if type(ci) is float:
            if ci<0 or ci>1:
                QMessageBox.warning(None, "参数设置错误", "变量ci必须设置在[0,1]。当前已被重置为0.95", QMessageBox.Ok)
                ci = 0.95
        else:
            ci =0.95
        paras.setdefault("ci",ci)
        self.task.set_worker(pg.cronbach_alpha, *lparas, **paras)