#   -*- coding:utf-8 -*-
#   The welch_anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:11 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Welch_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("One-way Welch ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.welch_anova.html#pingouin.welch_anova"
        self.log.info("welch_anova method!")

        self.show_add_parameter(2)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("between变量")

        self.show_choose_parameters(0)
        self.show_set_parameters(0)


    def start_analyse(self):
        paras = {}
        paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "独立变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("dv",dv[0])
        between = self.listView_2.model().stringList()
        if len(between) != 1:
            QMessageBox.warning(None, "参数设置错误", "between变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("between",between[0])

        self.task.set_worker(pg.welch_anova, **paras)