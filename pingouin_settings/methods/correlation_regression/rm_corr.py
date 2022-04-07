#   -*- coding:utf-8 -*-
#   The rm_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 18:01 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Rm_corr_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Repeated measures correlation")
        self.url = "https://pingouin-stats.org/generated/pingouin.rm_corr.html#pingouin.rm_corr"
        self.log.info("rm_corr method!")

        self.show_add_parameter(3)
        self.label_l1.setText("x")
        self.label_l2.setText("y")
        self.label_l3.setText("subject")

        self.show_choose_parameters(0)

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

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])

        self.task.set_worker(pg.rm_corr, *lparas, **paras)