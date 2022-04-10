#   -*- coding:utf-8 -*-
#   The power_chi2.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:44 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Power_chi2_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Evaluate power, sample size, effect size or significance level of chi-squared tests")
        self.url = "https://pingouin-stats.org/generated/pingouin.power_chi2.html#pingouin.power_chi2"
        self.log.info("power_chi2 method!")

        self.show_add_parameter(0)

        self.show_choose_parameters(0)

        self.show_set_parameters(5)
        self.label_s1.setText("dof")
        self.lineEdit_s1.setText("0")
        self.label_s2.setText("w")
        self.lineEdit_s2.setText("None")
        self.label_s3.setText("n")
        self.lineEdit_s3.setText("None")
        self.label_s4.setText("power")
        self.lineEdit_s4.setText("None")
        self.label_s5.setText("alpha")
        self.lineEdit_s5.setText("0.05")

    def start_analyse(self):
        lparas =()
        paras = {}

        try:
            dof =float(self.lineEdit_s1.text())
        except ValueError:
            dof = 0
        if not isinstance(dof, (int, float)):
            QMessageBox.warning(None, "参数设置错误", "变量dof必须设置成float或int类型。", QMessageBox.Ok)
            return
        paras.setdefault("dof",dof)

        try:
            w =float(self.lineEdit_s2.text())
        except ValueError:
            w = None
        if w is not None:
            if type(w) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量w必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                w = None
        paras.setdefault("w",w)

        try:
            n =int(self.lineEdit_s3.text())
        except ValueError:
            n = None
        if n is not None:
            if type(n) is not int:
                QMessageBox.warning(None, "参数设置错误", "变量n必须设置成int类型。当前已重置为None", QMessageBox.Ok)
                n = None
        paras.setdefault("n",n)

        try:
            power =float(self.lineEdit_s4.text())
        except ValueError:
            power = None
        if power is not None:
            if type(power) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量power必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                power = None
        paras.setdefault("power",power)

        try:
            alpha =float(self.lineEdit_s5.text())
        except ValueError:
            alpha = None
        if alpha is not None:
            if type(alpha) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                alpha= None
        paras.setdefault("alpha",alpha)

        n_none = sum([v is None for v in [w, n, power, alpha]])
        if n_none != 1:
            QMessageBox.warning(None, "参数设置错误", "变量w, n, power, alpha 最多只可以有一个为None", QMessageBox.Ok)
            return

        self.task.set_worker(pg.power_chi2, *lparas, **paras)