#   -*- coding:utf-8 -*-
#   The friedman.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:47 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Friedman_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Friedman test for repeated measurements")
        self.url = "https://pingouin-stats.org/generated/pingouin.friedman.html#pingouin.friedman"
        self.log.info("friedman method!")

        self.show_add_parameter(3)
        self.label_l1.setText("dv")
        self.label_l2.setText("within")
        self.label_l3.setText("subject")

        self.show_choose_parameters(1)
        self.label_p1.setText("method")
        self.comboBox_p1.addItem("chisq")
        self.comboBox_p1.addItem("f")


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

        within = self.listView_2.model().stringList()
        if len(within) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量within能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("within", within[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])
        paras.setdefault("method",self.comboBox_p1.currentText())

        self.task.set_worker(pg.friedman, *lparas, **paras)