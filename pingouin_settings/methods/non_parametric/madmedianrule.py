#   -*- coding:utf-8 -*-
#   The madmedianrule.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 21:30 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Madmedianrule_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Robust outlier detection based on the MAD-median rule")
        self.url = "https://pingouin-stats.org/generated/pingouin.madmedianrule.html#pingouin.madmedianrule"
        self.log.info("madmedianrule method!")

        self.show_add_parameter(1)
        self.label_l1.setText("a")

        self.show_choose_parameters(0)

        self.show_set_parameters(0)

    def start_analyse(self):
        paras = {}

        a = self.listView_1.model().stringList()
        if len(a) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("a",self.df[a[0]])

        self.task.set_worker(pg.madmedianrule, **paras)