#   -*- coding:utf-8 -*-
#   The kruskal.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:59 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Kruskal_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Kruskal-Wallis H-test for independent samples")
        self.url = "https://pingouin-stats.org/generated/pingouin.kruskal.html#pingouin.kruskal"
        self.log.info("kruskal method!")

        self.show_add_parameter(2)
        self.label_l1.setText("dv")
        self.label_l2.setText("between")

        self.show_choose_parameters(0)

        self.show_set_parameters(0)

    def start_analyse(self):
        lparas = ()
        # 将 self.df 赋值给lparas 会引起 got multiple values for argument 错误
        paras = {}
        paras.setdefault("data",self.df)

        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("dv",dv[0])

        between = self.listView_2.model().stringList()
        if len(between) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量between能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("between", between[0])

        self.task.set_worker(pg.kruskal, *lparas, **paras)