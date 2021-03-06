#   -*- coding:utf-8 -*-
#   The distance_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:14 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Distance_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Partial and semi-partial correlation.")
        self.url = "https://pingouin-stats.org/generated/pingouin.distance_corr.html#pingouin.distance_corr"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "distance_corr method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(2)
        self.label_l1.setText("x")
        self.label_l2.setText("y")

        self.show_choose_parameters(2)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("less")
        self.label_p2.setText("维数")
        self.comboBox_p2.addItem("1维")
        self.comboBox_p2.addItem("2维")

        self.show_set_parameters(2)
        self.label_s1.setText("n_boot")
        self.lineEdit_s1.setText("1000")
        self.label_s2.setText("随机种子")
        self.lineEdit_s2.setText("None")

    def start_analyse(self):
        self.paras.clear()

        if self.comboBox_p2.currentIndex()!=0:
            QMessageBox.warning(None, "功能未实现", "Pingouin支持2维数据的distance_corr计算，但UI移植尚未完成。", QMessageBox.Ok)
            return

        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("x",self.df[x[0]])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("y", self.df[y[0]])

        self.paras.setdefault("alternative",self.comboBox_p1.currentText())

        try:
            n_boot = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "n_boot需要被设置成整数，当前已重置为1000。", QMessageBox.Ok)
            n_boot = 1000
        if n_boot is not None or n_boot != 1000:
            try:
                n_boot = int(n_boot)
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "n_boot需要被设置成整数，当前已重置为1000。", QMessageBox.Ok)
                n_boot = 1000
        self.paras.setdefault("n_boot",n_boot)

        try:
            seed = eval(self.lineEdit_s2.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "n_boot需要被设置成整数，当前已重置为1000。", QMessageBox.Ok)
            seed = None
        if seed is not None:
            try:
                seed = int(seed)
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "n_boot需要被设置成整数，当前已重置为1000。", QMessageBox.Ok)
                seed = 1000
        self.paras.setdefault("seed",seed)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.distance_corr, **self.paras)