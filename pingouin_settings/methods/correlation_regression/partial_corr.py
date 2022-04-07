#   -*- coding:utf-8 -*-
#   The partial_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:47 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Partial_corr_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Partial and semi-partial correlation.")
        self.url = "https://pingouin-stats.org/generated/pingouin.partial_corr.html#pingouin.partial_corr"
        self.log.info("partial_corr method!")

        self.show_add_parameter(5)
        self.label_l1.setText("x")
        self.label_l2.setText("y")
        self.label_l3.setText("covar")
        self.label_l4.setText("x_covar")
        self.label_l5.setText("y_covar")

        self.show_choose_parameters(2)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")
        self.label_p2.setText("method")
        self.comboBox_p2.addItem("pearson")
        self.comboBox_p2.addItem("spearman")

        self.show_set_parameters(0)

    def start_analyse(self):
        lparas = ()
        # 将 self.df 赋值给lparas 会引起 got multiple values for argument 错误
        paras = {}
        paras.setdefault("data",self.df)

        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("x",x[0])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("y", y[0])

        count = 0

        covar = self.listView_3.model().stringList()
        if len(covar) > 1:
            paras.setdefault("covar", covar)
        elif len(covar) == 1:
            paras.setdefault("covar", covar[0])
        else:
            count = count + 1

        x_covar = self.listView_4.model().stringList()
        if len(x_covar) > 1:
            paras.setdefault("x_covar", x_covar)
        elif len(x_covar) == 1:
            paras.setdefault("x_covar", x_covar[0])
        else:
            count = count + 1

        y_covar = self.listView_5.model().stringList()
        if len(y_covar) > 1:
            paras.setdefault("y_covar", y_covar)
        elif len(y_covar) == 1:
            paras.setdefault("y_covar", y_covar[0])
        else:
            count = count + 1

        if count != 2:
            QMessageBox.warning(None, "参数设置错误", "单次统计时，只能从变量covar、x_covar及y_covar中设置一个。", QMessageBox.Ok)
            return

        paras.setdefault("alternative",self.comboBox_p1.currentText())
        paras.setdefault("method", self.comboBox_p2.currentText())

        self.task.set_worker(pg.partial_corr, *lparas, **paras)