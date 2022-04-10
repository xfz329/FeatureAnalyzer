#   -*- coding:utf-8 -*-
#   The anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:02 on 2022/4/2

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Anova_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("One-way and N-way ANOVA")
        self.url = "https://pingouin-stats.org/generated/pingouin.anova.html#pingouin.anova"
        self.log.info("anova method!")

        self.show_add_parameter(2)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("检测变量")

        self.show_choose_parameters(3)
        self.label_p1.setText("平方和类型")
        self.comboBox_p1.addItem("1")
        self.comboBox_p1.addItem("2")
        self.comboBox_p1.addItem("3")
        self.label_p2.setText("返回详细值")
        self.comboBox_p2.addItem("详细")
        self.comboBox_p2.addItem("简略")
        self.label_p3.setText("效应值")
        self.comboBox_p3.addItem("偏η2")
        self.comboBox_p3.addItem("η2")

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
        if len(between) == 0:
            QMessageBox.warning(None, "参数设置错误", "至少需要设置一个检测变量。",QMessageBox.Ok)
            return
        paras.setdefault("between",between)
        paras.setdefault("ss_type",self.comboBox_p1.currentIndex()+1)
        paras.setdefault("detailed",self.comboBox_p2.currentIndex()==0)
        if self.comboBox_p3.currentIndex() == 0:
            effsize = "np2"
        else:
            effsize ="n2"
        paras.setdefault("effsize",effsize)

        self.task.set_worker(pg.anova, **paras)
