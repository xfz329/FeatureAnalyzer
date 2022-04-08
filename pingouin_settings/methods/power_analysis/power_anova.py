#   -*- coding:utf-8 -*-
#   The power_anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:23 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Power_anova_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Evaluate power, sample size, effect size or significance level of a one-way balanced ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.power_anova.html#pingouin.power_anova"
        self.log.info("power_anova method!")

        self.show_add_parameter(0)

        self.show_choose_parameters(0)

        self.show_set_parameters(5)
        self.label_s1.setText("eta")
        self.lineEdit_s1.setText("None")
        self.label_s2.setText("k")
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
            eta =float(self.lineEdit_s1.text())
        except ValueError:
            eta = None
        if eta is not None:
            if type(eta) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量eta必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                eta = None
        paras.setdefault("eta",eta)

        try:
            k =int(self.lineEdit_s2.text())
        except ValueError:
            k = None
        if k is not None:
            if type(k) is not int:
                QMessageBox.warning(None, "参数设置错误", "变量k必须设置成int类型。当前已重置为None", QMessageBox.Ok)
                k = None
        paras.setdefault("k",k)

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

        n_none = sum([v is None for v in [eta, k, n, power, alpha]])
        if n_none != 1:
            QMessageBox.warning(None, "参数设置错误", "变量eta, k, n, power, alpha 最多只可以有一个为None", QMessageBox.Ok)
            return

        self.task.set_worker(pg.power_anova, *lparas, **paras)