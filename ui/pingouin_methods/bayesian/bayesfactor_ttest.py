#   -*- coding:utf-8 -*-
#   The bayesfactor_ttest.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:29 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Bayesfactor_ttest_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Bayes Factor of a T-test.")
        self.url = "https://pingouin-stats.org/generated/pingouin.bayesfactor_ttest.html#pingouin.bayesfactor_ttest"
        self.log.info("bayesfactor_ttest method!")


        self.show_add_parameter(2)
        self.label_l1.setEnabled(False)
        self.listView_1.setEnabled(False)
        self.label_l2.setEnabled(False)
        self.listView_2.setEnabled(False)

        self.show_choose_parameters(2)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")

        self.label_p2.setText("paired")
        self.comboBox_p2.addItem("否")
        self.comboBox_p2.addItem("是")

        self.show_set_parameters(4)
        self.label_s1.setText("T-value t")
        self.label_s2.setText("采样数 x")
        self.label_s3.setText("采样数 y")
        self.label_s4.setText("r")
        self.lineEdit_s4.setText("0.707")



    def start_analyse(self):
        try:
            t = float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "t需要被设置成float类型的数值。", QMessageBox.Ok)
            return

        try:
            nx = int(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "nx需要被设置成int类型的数值。", QMessageBox.Ok)
            return

        lparas = (t, nx)
        paras = {}

        try:
            ny = int(self.lineEdit_s3.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "ny需要被设置成int类型的数值。ny当前值已被设置成None，如需调整，请在设置后重新开始分析。", QMessageBox.Ok)
            ny = None

        paras.setdefault("ny",ny)

        if self.comboBox_p1.currentIndex() == 0:
            alternative = "two-sided"
        elif self.comboBox_p1.currentIndex() == 1:
            alternative = "greater"
        else:
            alternative ="less"
        paras.setdefault("alternative",alternative)
        paras.setdefault("paired",self.comboBox_p2.currentIndex() == 1)

        try:
            r = float(self.lineEdit_s4.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "r需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("r", r)
        self.task.set_worker(pg.bayesfactor_ttest, *lparas, **paras)