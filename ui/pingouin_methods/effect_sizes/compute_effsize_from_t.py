#   -*- coding:utf-8 -*-
#   The compute_effsize_from_t.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:10 on 2022/4/10

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Compute_effsize_from_t_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Compute effect size from a T-value")
        self.url = "https://pingouin-stats.org/generated/pingouin.compute_effsize_from_t.html#pingouin.compute_effsize_from_t"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "compute_effsize_from_t method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(0)

        self.show_choose_parameters(1)
        self.label_p1.setText("eftype")
        self.comboBox_p1.addItem("cohen")
        self.comboBox_p1.addItem("none")
        self.comboBox_p1.addItem("hedges")
        self.comboBox_p1.addItem("r")
        self.comboBox_p1.addItem("eta-square")
        self.comboBox_p1.addItem("AUC")
        self.comboBox_p1.addItem("CLES")


        self.show_set_parameters(4)
        self.label_s1.setText("tval")
        self.label_s2.setText("nx")
        self.lineEdit_s2.setText("None")
        self.label_s3.setText("ny")
        self.lineEdit_s3.setText("None")
        self.label_s4.setText("N")
        self.lineEdit_s4.setText("None")


    def start_analyse(self):
        self.paras.clear()

        self.paras.setdefault("eftype",self.comboBox_p1.currentText())

        try:
            tval = float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "tval需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("tval",tval)

        try:
            nx = eval(self.lineEdit_s2.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "nx需要被设置成int或None类型的数值。", QMessageBox.Ok)
            nx = None
        if nx is not None:
            try:
                nx = int(nx)
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "nx需要被设置成int或None类型的数值。", QMessageBox.Ok)
                return
        self.paras.setdefault("nx",nx)

        try:
            ny = eval(self.lineEdit_s3.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "ny需要被设置成int或None类型的数值。", QMessageBox.Ok)
            ny = None
        if ny is not None:
            try:
                ny = int(ny)
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "ny需要被设置成int或None类型的数值。", QMessageBox.Ok)
                return
        self.paras.setdefault("ny",ny)

        try:
            N = eval(self.lineEdit_s4.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "N需要被设置成int或None类型的数值。", QMessageBox.Ok)
            N = None
        if N is not None:
            try:
                N = int(N)
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "N需要被设置成int或None类型的数值。", QMessageBox.Ok)
                return
        self.paras.setdefault("N",N)

        self.paras.setdefault("tval",tval)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.compute_effsize_from_t, **self.paras)