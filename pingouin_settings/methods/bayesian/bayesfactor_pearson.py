#   -*- coding:utf-8 -*-
#   The bayesfactor_pearson.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:52 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Bayesfactor_pearson_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Bayes Factor of a Pearson correlation")
        self.url = "https://pingouin-stats.org/generated/pingouin.bayesfactor_pearson.html#pingouin.bayesfactor_pearson"
        self.log.info("bayesfactor_pearson method!")


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

        self.label_p2.setText("method")
        self.comboBox_p2.addItem("ly")
        self.comboBox_p2.addItem("wetzels")

        self.show_set_parameters(3)
        self.label_s1.setText("Pearson correlation coefficient r")
        self.label_s2.setText("Sample size n")
        self.label_s3.setText("kappa factor")
        self.lineEdit_s3.setText("1.0")



    def start_analyse(self):
        try:
            r = float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "r需要被设置成float类型的数值。", QMessageBox.Ok)
            return

        try:
            n = int(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "n需要被设置成int类型的数值。", QMessageBox.Ok)
            return

        lparas = (r, n)
        paras = {}

        if self.comboBox_p1.currentIndex() == 0:
            alternative = "two-sided"
        elif self.comboBox_p1.currentIndex() == 1:
            alternative = "greater"
        else:
            alternative ="less"
        paras.setdefault("alternative",alternative)

        method = self.comboBox_p2.currentText()
        paras.setdefault("method", method)
        if method == 'ly':
            try:
                kappa = float(self.lineEdit_s3.text())
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "kappa需要被设置成float类型的数值。", QMessageBox.Ok)
                return
        else:
            QMessageBox.warning(None, "参数设置提醒", "kappa在wetzels方法下已被禁用，分析继续。", QMessageBox.Ok)
            kappa = 1.0
        paras.setdefault("kappa",kappa)

        self.task.set_worker(pg.bayesfactor_pearson, *lparas, **paras)