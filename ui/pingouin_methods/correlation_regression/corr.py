#   -*- coding:utf-8 -*-
#   The corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 13:02 on 2022/4/7


from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("(Robust) correlation between two variables")
        self.url = "https://pingouin-stats.org/generated/pingouin.corr.html#pingouin.corr"
        self.log.info("corr method!")


        self.show_add_parameter(2)
        self.label_l1.setText("变量x")
        self.label_l2.setText("变量y")

        self.show_choose_parameters(2)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")


        self.label_p2.setText("method")
        self.comboBox_p2.addItem("pearson")
        self.comboBox_p2.addItem("spearman")
        self.comboBox_p2.addItem("kendall")
        self.comboBox_p2.addItem("bicor")
        self.comboBox_p2.addItem("percbend")
        self.comboBox_p2.addItem("shepherd")
        self.comboBox_p2.addItem("skipped")

        self.show_set_parameters(1)
        self.label_s1.setText("kwargs")

    def start_analyse(self):
        xv = self.listView_1.model().stringList()
        if len(xv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        x = self.df[xv[0]]

        yv = self.listView_2.model().stringList()
        if len(yv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        y = self.df[yv[0]]

        lparas = (x,y)
        paras = {}

        paras.setdefault("alternative",self.comboBox_p1.currentText())
        paras.setdefault("method", self.comboBox_p2.currentText())

        try:
            kws = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成dict类型的数值。当前kwargs已被设置成空dict，分析继续。", QMessageBox.Ok)
            kws = {}
        if type(kws) is not dict:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成dict类型的数值。当前kwargs已被设置成空dict，分析继续。", QMessageBox.Ok)
            kws = {}
        for key in kws:
            paras.setdefault(key,kws[key])
        self.task.set_worker(pg.corr, *lparas, **paras)

# if __name__ =="__main__":
#     import numpy as np
#
#     # Generate random correlated samples
#     np.random.seed(123)
#     mean, cov = [4, 6], [(1, .5), (.5, 1)]
#     x, y = np.random.multivariate_normal(mean, cov, 30).T
#     print(x[3])
#     print(type(x))
#     print("**********")
#     print(y[5])
#     print(type(y))