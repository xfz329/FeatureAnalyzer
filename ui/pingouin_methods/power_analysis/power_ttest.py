#   -*- coding:utf-8 -*-
#   The power_ttest.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 17:20 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Power_ttest_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Evaluate power, sample size, effect size or significance level of a one-sample T-test, a paired T-test or an independent two-samples T-test with equal sample sizes")
        self.url = "https://pingouin-stats.org/generated/pingouin.power_ttest.html#pingouin.power_ttest"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "power_ttest method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(0)

        self.show_choose_parameters(2)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")
        self.label_p2.setText("contrast")
        self.comboBox_p2.addItem("two-samples")
        self.comboBox_p2.addItem("one-sample")
        self.comboBox_p2.addItem("paired")

        self.show_set_parameters(4)
        self.label_s1.setText("d")
        self.lineEdit_s1.setText("None")
        self.label_s2.setText("n")
        self.lineEdit_s2.setText("None")
        self.label_s3.setText("power")
        self.lineEdit_s3.setText("None")
        self.label_s4.setText("alpha")
        self.lineEdit_s4.setText("0.05")


    def start_analyse(self):
        self.paras.clear()

        self.paras.setdefault("alternative",self.comboBox_p1.currentText())
        self.paras.setdefault("contrast",self.comboBox_p2.currentText())

        try:
            d =float(self.lineEdit_s1.text())
        except ValueError:
            d = None
        if d is not None:
            if type(d) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量d必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                r = None
        self.paras.setdefault("d",d)

        try:
            n =int(self.lineEdit_s2.text())
        except ValueError:
            n = None
        if n is not None:
            if type(n) is not int:
                QMessageBox.warning(None, "参数设置错误", "变量n必须设置成int类型。当前已重置为None", QMessageBox.Ok)
                n = None
        self.paras.setdefault("n",n)

        try:
            power =float(self.lineEdit_s3.text())
        except ValueError:
            power = None
        if power is not None:
            if type(power) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量power必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                power = None
        self.paras.setdefault("power",power)

        try:
            alpha =float(self.lineEdit_s4.text())
        except ValueError:
            alpha = None
        if alpha is not None:
            if type(alpha) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                alpha= None
        self.paras.setdefault("alpha",alpha)

        n_none = sum([v is None for v in [d, n, power, alpha]])
        if n_none != 1:
            QMessageBox.warning(None, "参数设置错误", "变量d, n, power, alpha 最多只可以有一个为None", QMessageBox.Ok)
            return

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.power_ttest, **self.paras)