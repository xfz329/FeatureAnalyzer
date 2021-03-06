#   -*- coding:utf-8 -*-
#   The convert_effsize.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:25 on 2022/4/10

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Convert_effsize_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Compute effect size from a T-value")
        self.url = "https://pingouin-stats.org/generated/pingouin.compute_effsize_from_t.html#pingouin.compute_effsize_from_t"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "convert_effsize method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(0)

        self.show_choose_parameters(2)
        self.label_p1.setText("input_type")
        self.comboBox_p1.addItem("r")
        self.comboBox_p1.addItem("cohen")
        self.label_p2.setText("output_type")
        self.comboBox_p2.addItem("cohen")
        self.comboBox_p2.addItem("hedges")
        self.comboBox_p2.addItem("eta-square")
        self.comboBox_p2.addItem("AUC")
        self.comboBox_p2.addItem("none")


        self.show_set_parameters(3)
        self.label_s1.setText("ef")
        self.label_s2.setText("nx")
        self.lineEdit_s2.setText("None")
        self.label_s3.setText("ny")
        self.lineEdit_s3.setText("None")


    def start_analyse(self):
        self.paras.clear()

        self.paras.setdefault("input_type",self.comboBox_p1.currentText())
        self.paras.setdefault("output_type",self.comboBox_p2.currentText())

        try:
            ef = float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "ef需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("ef",ef)

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

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.convert_effsize, **self.paras)