#   -*- coding:utf-8 -*-
#   The rm_anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 13:37 on 2022/4/6
from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_RM_Anova_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("One-way and two-way repeated measures ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.rm_anova.html#pingouin.rm_anova"
        self.log.info("rm_anova method!")

        self.show_add_parameter(3)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("within")
        self.label_l3.setText("subject")

        self.show_choose_parameters(3)
        self.label_p1.setText("效应值")
        self.comboBox_p1.addItem("偏η2")
        self.comboBox_p1.addItem("η2")
        self.comboBox_p1.addItem("ηg2")
        self.label_p2.setText("修正")
        self.comboBox_p2.addItem("auto")
        self.comboBox_p2.addItem("True")
        self.label_p3.setText("返回详细值")
        self.comboBox_p3.addItem("详细")
        self.comboBox_p3.addItem("简略")

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
        if len(within) == 1:
            paras.setdefault("within", within[0])
        elif len(within) == 2:
            paras.setdefault("within", within)
        else:
            QMessageBox.warning(None, "参数设置错误", "within变量只能设置为一个或两个。",QMessageBox.Ok)
            return
        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "subject变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])

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
        paras.setdefault("detailed", self.comboBox_p3.currentIndex() == 0)

        self.task.set_worker(pg.rm_anova, **paras)