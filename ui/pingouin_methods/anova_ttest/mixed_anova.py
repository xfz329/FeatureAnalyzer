#   -*- coding:utf-8 -*-
#   The mixed_anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:57 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Mixed_Anova_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Mixed-design (split-plot) ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.mixed_anova.html#pingouin.mixed_anova"
        self.log.info("mixed_anova method!")

        self.show_add_parameter(4)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("within")
        self.label_l3.setText("subject")
        self.label_l4.setText("between")

        self.show_choose_parameters(2)
        self.label_p1.setText("效应值")
        self.comboBox_p1.addItem("偏η2")
        self.comboBox_p1.addItem("η2")
        self.comboBox_p1.addItem("ηg2")
        self.label_p2.setText("修正")
        self.comboBox_p2.addItem("auto")
        self.comboBox_p2.addItem("True")

        self.show_set_parameters(0)


    def start_analyse(self):
        paras = {}
        paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "独立变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("dv",dv[0])
        within = self.listView_2.model().stringList()
        if len(within) != 1:
            QMessageBox.warning(None, "参数设置错误", "within变量只能设置为一个或两个。",QMessageBox.Ok)
            return
        paras.setdefault("within", within[0])
        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "subject变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])
        between = self.listView_4.model().stringList()
        if len(between) != 1:
            QMessageBox.warning(None, "参数设置错误", "between变量能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("between", between[0])

        if self.comboBox_p1.currentIndex() == 0:
            effsize = "np2"
        elif self.comboBox_p1.currentIndex() == 1:
            effsize = "n2"
        else:
            effsize ="ng2"
        paras.setdefault("effsize",effsize)

        if self.comboBox_p2.currentIndex() == 0:
            correction = "auto"
        else:
            correction = True
        paras.setdefault("correction",correction)

        self.task.set_worker(pg.mixed_anova, **paras)