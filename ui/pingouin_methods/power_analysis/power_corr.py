#   -*- coding:utf-8 -*-
#   The power_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 17:08 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Power_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Evaluate power, sample size, correlation coefficient or significance level of a correlation test")
        self.url = "https://pingouin-stats.org/generated/pingouin.power_corr.html#pingouin.power_corr"
        self.log.info("power_corr method!")

        self.show_add_parameter(0)

        self.show_choose_parameters(1)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")

        self.show_set_parameters(4)
        self.label_s1.setText("r")
        self.lineEdit_s1.setText("None")
        self.label_s2.setText("n")
        self.lineEdit_s2.setText("None")
        self.label_s3.setText("power")
        self.lineEdit_s3.setText("None")
        self.label_s4.setText("alpha")
        self.lineEdit_s4.setText("0.05")



    def start_analyse(self):
        lparas =()
        paras = {}

        paras.setdefault("alternative",self.comboBox_p1.currentText())

        try:
            r =float(self.lineEdit_s1.text())
        except ValueError:
            r = None
        if r is not None:
            if type(r) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量r必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                r = None
        paras.setdefault("r",r)

        try:
            n =int(self.lineEdit_s2.text())
        except ValueError:
            n = None
        if n is not None:
            if type(n) is not int:
                QMessageBox.warning(None, "参数设置错误", "变量n必须设置成int类型。当前已重置为None", QMessageBox.Ok)
                n = None
        paras.setdefault("n",n)

        try:
            power =float(self.lineEdit_s3.text())
        except ValueError:
            power = None
        if power is not None:
            if type(power) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量power必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                power = None
        paras.setdefault("power",power)

        try:
            alpha =float(self.lineEdit_s4.text())
        except ValueError:
            alpha = None
        if alpha is not None:
            if type(alpha) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                alpha= None
        paras.setdefault("alpha",alpha)

        n_none = sum([v is None for v in [r, n, power, alpha]])
        if n_none != 1:
            QMessageBox.warning(None, "参数设置错误", "变量r, n, power, alpha 最多只可以有一个为None", QMessageBox.Ok)
            return

        self.task.set_worker(pg.power_corr, *lparas, **paras)