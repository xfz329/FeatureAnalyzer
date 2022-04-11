#   -*- coding:utf-8 -*-
#   The qqplot.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 22:51 on 2022/4/9

import os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin
import data.Globalvar as gl

class Ui_Qqplot_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Quantile-Quantile plot")
        self.url = "https://pingouin-stats.org/generated/pingouin.qqplot.html#pingouin.qqplot"
        self.log.info("qqplot method!")

        self.desc.setdefault("detail", "Quantile-Quantile plot")
        self.desc.setdefault("brief", "qqplot method!")
        self.desc.setdefault("url", self.url)

        self.show_add_parameter(1)
        self.label_l1.setText("x")

        self.show_choose_parameters(0)

        self.show_set_parameters(2)
        self.label_s1.setText("dist")
        self.lineEdit_s1.setText("norm")
        self.label_s2.setText("confidence")
        self.lineEdit_s2.setText("0.95")


    def start_analyse(self):
        self.paras.clear()
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        x = self.df[x[0]]

        # import numpy as np
        # import pingouin as pg
        # np.random.seed(123)
        # x = np.random.normal(size=50)

        self.paras.setdefault('x',x)
        self.paras.setdefault("dist",self.lineEdit_s1.text())

        try:
            confidence = float(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "confidence需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("confidence", confidence)

        win = gl.get_value("Win_manager").get_sub_window("Window_Matplot")
        win.get_canvas().figure.clf()
        self.log.info("The Window_Matplot is "+str(win))
        ax = win.get_canvas().figure.subplots()
        self.paras.setdefault("ax", ax)

        self.desc["start_time"] = QDateTime.currentDateTime().toString("HH:mm:ss.zzz")
        pg.qqplot(**self.paras)
        win.get_canvas().draw()
        win.get_canvas().flush_events()
        name = "Fig_" + QDateTime.currentDateTime().toString("yyMMdd_HHmmss") + ".jpg"
        full_name = os.path.join(gl.get_value("FIG_PATH"), name)
        win.get_canvas().figure.savefig(full_name)
        self.desc['path'] = full_name
        self.info_draw_finished()