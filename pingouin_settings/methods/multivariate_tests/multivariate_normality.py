#   -*- coding:utf-8 -*-
#   The multivariate_normality.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:47 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Multivariate_normality_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Henze-Zirkler multivariate normality test")
        self.url = "https://pingouin-stats.org/generated/pingouin.multivariate_normality.html#pingouin.multivariate_normality"
        self.log.info("multivariate_normality method!")

        self.show_add_parameter(1)
        self.label_l1.setText("X")

        self.show_choose_parameters(0)

        self.show_set_parameters(1)
        self.label_s1.setText("alpha")
        self.lineEdit_s1.setText("0.05")

    def start_analyse(self):
        lparas =()
        paras = {}

        x = self.listView_1.model().stringList()
        paras.setdefault("X",self.df[x])

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
        paras.setdefault("alpha",alpha)
        self.task.set_worker(pg.multivariate_normality, *lparas, **paras)