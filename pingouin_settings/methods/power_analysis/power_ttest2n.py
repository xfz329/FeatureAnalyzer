#   -*- coding:utf-8 -*-
#   The power_ttest2n.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 17:21 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Power_ttest2n_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Evaluate power, effect size or significance level of an independent two-samples T-test with unequal sample sizes.")
        self.url = "https://pingouin-stats.org/generated/pingouin.power_ttest2n.html#pingouin.power_ttest2n"
        self.log.info("power_ttest2n method!")

        self.show_add_parameter(0)

        self.show_choose_parameters(1)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")

        self.show_set_parameters(5)
        self.label_s1.setText("nx")
        self.label_s2.setText("ny")
        self.label_s3.setText("d")
        self.lineEdit_s3.setText("None")
        self.label_s4.setText("power")
        self.lineEdit_s4.setText("None")
        self.label_s5.setText("alpha")
        self.lineEdit_s5.setText("0.05")



    def start_analyse(self):
        lparas =()
        paras = {}

        paras.setdefault("alternative",self.comboBox_p1.currentText())

        try:
            nx = int(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "变量nx必须设置成int类型,请重新设置！", QMessageBox.Ok)
            return
        paras.setdefault("nx",nx)

        try:
            ny = int(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "变量ny必须设置成int类型,请重新设置！", QMessageBox.Ok)
            return
        paras.setdefault("ny",ny)

        if nx == ny :
            QMessageBox.warning(None, "参数设置错误", "变量nx与ny的值不能相等！若值必须相等，请考虑使用power_ttest方法！", QMessageBox.Ok)
            return

        try:
            d =float(self.lineEdit_s3.text())
        except ValueError:
            d = None
        if d is not None:
            if type(d) is not float:
                QMessageBox.warning(None, "参数设置错误", "变量d必须设置成float类型。当前已重置为None", QMessageBox.Ok)
                d = None
        paras.setdefault("d",d)

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

        n_none = sum([v is None for v in [d, power, alpha]])
        if n_none != 1:
            QMessageBox.warning(None, "参数设置错误", "变量 d, power, alpha 最多只可以有一个为None", QMessageBox.Ok)
            return

        self.task.set_worker(pg.power_ttest2n, *lparas, **paras)