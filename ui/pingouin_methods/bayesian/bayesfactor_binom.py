#   -*- coding:utf-8 -*-
#   The bayesfactor_binom.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:11 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Bayesfactor_binom_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Bayes factor of a binomial test with k successes, n trials and base probability p.")
        self.url = "https://pingouin-stats.org/generated/pingouin.bayesfactor_binom.html#pingouin.bayesfactor_binom"
        self.log.info("bayesfactor_binom method!")


        self.show_add_parameter(2)
        self.label_l1.setEnabled(False)
        self.listView_1.setEnabled(False)
        self.label_l2.setEnabled(False)
        self.listView_2.setEnabled(False)

        self.show_choose_parameters(0)

        self.show_set_parameters(3)
        self.label_s1.setText("成功次数k")
        self.label_s2.setText("总实验数n")
        self.label_s2.setText("基础成功概率p")


    def start_analyse(self):
        try:
            k = int(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "k需要被设置成int类型的数值。", QMessageBox.Ok)
            return

        try:
            n = int(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "n需要被设置成int类型的数值。", QMessageBox.Ok)
            return

        try:
            p = float(self.lineEdit_s3.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "p需要被设置成[0,1]区间内的float类型的数值。", QMessageBox.Ok)
            return
        if p > 1 or p < 0:
            QMessageBox.warning(None, "参数设置错误", "p需要被设置成[0,1]区间内的float类型的数值。", QMessageBox.Ok)
            return
        lparas = (k, n)
        paras = {"p":p}
        self.task.set_worker(pg.bayesfactor_binom, *lparas, **paras)