#   -*- coding:utf-8 -*-
#   The power_rm_anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:16 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Power_rm_anova_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Evaluate power, sample size, effect size or significance level of a balanced one-way repeated measures ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.power_rm_anova.html#pingouin.power_rm_anova"
        self.log.info("power_rm_anova method!")

        self.show_add_parameter(0)

        self.show_choose_parameters(0)

        self.show_set_parameters(7)
        self.label_s1.setText("eta")
        self.lineEdit_s1.setText("None")
        self.label_s2.setText("m")
        self.lineEdit_s2.setText("None")
        self.label_s3.setText("n")
        self.lineEdit_s3.setText("None")
        self.label_s4.setText("power")
        self.lineEdit_s4.setText("None")
        self.label_s5.setText("alpha")
        self.lineEdit_s5.setText("0.05")
        self.label_s6.setText("corr")
        self.lineEdit_s6.setText("0.5")
        self.label_s7.setText("epsilon")
        self.lineEdit_s7.setText("1")


    def start_analyse(self):
        lparas =()
        paras = {}

        try:
            eta =float(self.lineEdit_s1.text())
        except ValueError:
            eta = None
        if eta is not None:
            if type(eta) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量eta必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                eta = None
        paras.setdefault("eta",eta)

        try:
            m =int(self.lineEdit_s2.text())
        except ValueError:
            m = None
        if m is not None:
            if type(m) is not int:
                QMessageBox.warning(None, "参数设置错误", "变量m必须设置成int类型。当前已重置为None", QMessageBox.Ok)
                m = None
        paras.setdefault("m",m)

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

        try:
            corr =float(self.lineEdit_s6.text())
        except ValueError:
            corr = None
        if corr is not None:
            if type(corr) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量corr必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                corr= None
        paras.setdefault("corr",corr)

        try:
            epsilon =float(self.lineEdit_s7.text())
        except ValueError:
            epsilon = None
        if epsilon is not None:
            if type(epsilon) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量epsilon必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                epsilon= None
        paras.setdefault("epsilon",epsilon)

        n_none = sum([v is None for v in [eta, m, n, power, alpha]])
        if n_none != 1:
            QMessageBox.warning(None, "参数设置错误", "变量eta, k, n, power, alpha 最多只可以有一个为None", QMessageBox.Ok)
            return

        self.task.set_worker(pg.power_rm_anova, *lparas, **paras)