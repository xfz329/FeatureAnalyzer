#   -*- coding:utf-8 -*-
#   The mad.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 20:03 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Mad_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Median Absolute Deviation (MAD) along given axis of an array")
        self.url = "https://pingouin-stats.org/generated/pingouin.mad.html#pingouin.mad"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "mad method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(1)
        self.label_l1.setText("a")

        self.show_choose_parameters(1)
        self.label_p1.setText("normalize")
        self.comboBox_p1.addItem("True")
        self.comboBox_p1.addItem("False")

        self.show_set_parameters(1)
        self.label_s1.setText("axis")
        self.lineEdit_s1.setText("0")

    def start_analyse(self):
        # TODO 2D-array
        self.paras.clear()

        a = self.listView_1.model().stringList()
        if len(a) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("a",self.df[a[0]])

        self.paras.setdefault("normalize", self.comboBox_p1.currentIndex()==0)

        try:
            axis = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "axis需要被设置成整数或None，当前已重置为0。", QMessageBox.Ok)
            axis = 0
        if axis !=0:
            if axis is not None:
                try:
                    axis = int(axis)
                except ValueError:
                    QMessageBox.warning(None, "参数设置错误", "axis需要被设置成整数或None，当前已重置为0。", QMessageBox.Ok)
                    axis = 0
        self.paras.setdefault("axis", axis)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.mad, **self.paras)