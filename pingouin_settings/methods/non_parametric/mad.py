#   -*- coding:utf-8 -*-
#   The mad.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 20:03 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Mad_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Median Absolute Deviation (MAD) along given axis of an array")
        self.url = "https://pingouin-stats.org/generated/pingouin.mad.html#pingouin.mad"
        self.log.info("mad method!")

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
        paras = {}

        a = self.listView_1.model().stringList()
        if len(a) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("a",self.df[a[0]])

        paras.setdefault("normalize", self.comboBox_p1.currentIndex()==0)

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
        paras.setdefault("axis", axis)
        self.task.set_worker(pg.mad, **paras)