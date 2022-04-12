#   -*- coding:utf-8 -*-
#   The ancova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 1:49 on 2022/4/5
import pingouin as pg

from PyQt5.QtWidgets import QMessageBox

from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Ancova_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("ANCOVA with one or more covariate(s)")
        self.url = "https://pingouin-stats.org/generated/pingouin.ancova.html#pingouin.ancova"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "ancova method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(3)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("检测变量")
        self.label_l3.setText("协变量")

        self.show_choose_parameters(1)
        self.label_p1.setText("效应值")
        self.comboBox_p1.addItem("偏η2")
        self.comboBox_p1.addItem("η2")

        self.show_set_parameters(0)


    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "独立变量能且只能设置一个。",QMessageBox.Ok)
            return
        self.paras.setdefault("dv",dv[0])
        between = self.listView_2.model().stringList()
        if len(between) != 1:
            QMessageBox.warning(None, "参数设置错误", "检测变量能且只能设置一个。",QMessageBox.Ok)
            return
        self.paras.setdefault("between",between[0])
        covar = self.listView_3.model().stringList()
        if len(covar) == 0:
            QMessageBox.warning(None, "参数设置错误", "至少需要设置一个协变量。",QMessageBox.Ok)
            return
        self.paras.setdefault("covar", covar)
        if self.comboBox_p1.currentIndex() == 0:
            effsize = "np2"
        else:
            effsize ="n2"
        self.paras.setdefault("effsize",effsize)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.ancova, **self.paras)