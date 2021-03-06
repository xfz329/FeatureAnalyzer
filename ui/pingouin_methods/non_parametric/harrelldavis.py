#   -*- coding:utf-8 -*-
#   The harrelldavis.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 22:11 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Harrelldavis_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Harrell-Davis robust estimate of the qth quantile(s) of the data")
        self.url = "https://pingouin-stats.org/generated/pingouin.harrelldavis.html#pingouin.harrelldavis"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "harrelldavis method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(1)
        self.label_l1.setText("x")

        self.show_choose_parameters(1)
        self.label_p1.setText("axis")
        self.comboBox_p1.addItem("-1")
        self.comboBox_p1.addItem("0")
        self.comboBox_p1.addItem("1")

        self.show_set_parameters(1)
        self.label_s1.setText("quantile")
        self.lineEdit_s1.setText("0.5")

    def start_analyse(self):
        # TODO 2D
        self.paras.clear()
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("x",self.df[x[0]])

        self.paras.setdefault("axis", self.comboBox_p1.currentIndex()-1)

        try:
            quantile = eval(self.lineEdit_s1.text())
            print(quantile)
            print(type(quantile))
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "quantile需要被设置成float类型或数组，当前已重置为0.5。", QMessageBox.Ok)
            quantile = 0.5
        if  type(quantile) is float or type(quantile) is int:
            if quantile<0 or quantile>1 :
                QMessageBox.warning(None, "参数设置错误", "quantile需要被设置在[0,1]之间，当前已重置为0.5。", QMessageBox.Ok)
                quantile = 0.5
        elif type(quantile) is list:
            for l in quantile:
                if l < 0 or l > 1:
                    QMessageBox.warning(None, "参数设置错误", "quantile list中的每个值需要被设置在[0,1]之间，当前已重置为0.5。", QMessageBox.Ok)
                    quantile = 0.5
                    break
        else:
            quantile = 0.5
        self.paras.setdefault("quantile", quantile)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.harrelldavis, **self.paras)