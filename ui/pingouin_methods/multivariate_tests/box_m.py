#   -*- coding:utf-8 -*-
#   The box_m.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:46 on 2022/4/8

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin

class Ui_Box_m_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Test equality of covariance matrices using the Box’s M test.")
        self.url = "https://pingouin-stats.org/generated/pingouin.box_m.html#pingouin.box_m"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "box_m method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(2)
        self.label_l1.setText("dvs")
        self.label_l2.setText("group")

        self.show_choose_parameters(0)

        self.show_set_parameters(1)
        self.label_s1.setText("alpha")
        self.lineEdit_s1.setText("0.001")

    def start_analyse(self):
        # TODO unchecked function
        self.paras.clear()

        dvs = self.listView_1.model().stringList()
        self.paras.setdefault("dvs",dvs)

        group = self.listView_2.model().stringList()
        self.paras.setdefault("group", group[0])

        try:
            alpha =float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置成float类型。当前已被重置为0.001", QMessageBox.Ok)
            alpha = 0.001
        if type(alpha) is float:
            if alpha<0 or alpha>1:
                QMessageBox.warning(None, "参数设置错误", "变量alpha必须设置在[0,1]。当前已被重置为0.001", QMessageBox.Ok)
                alpha = 0.001
        else:
            alpha = 0.001
        self.paras.setdefault("alpha",alpha)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.box_m, **self.paras)