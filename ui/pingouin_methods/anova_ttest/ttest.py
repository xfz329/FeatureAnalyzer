#   -*- coding:utf-8 -*-
#   The ttest.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:55 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Ttest_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.single_y = False

    def set_widgets(self):
        self.label_method.setText("T-test")
        self.url = "https://pingouin-stats.org/generated/pingouin.ttest.html#pingouin.ttest"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "ttest method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(2)
        self.label_l1.setText("变量x")
        self.label_l2.setText("变量y")

        self.show_choose_parameters(4)
        self.label_p1.setText("y变量数据类型")
        self.comboBox_p1.addItem("列表")
        self.comboBox_p1.addItem("单值")
        self.comboBox_p1.currentIndexChanged.connect(self.adjustY)

        self.label_p2.setText("paired")
        self.comboBox_p2.addItem("False")
        self.comboBox_p2.addItem("True")

        self.label_p3.setText("alternative")
        self.comboBox_p3.addItem("two-sided")
        self.comboBox_p3.addItem("greater")
        self.comboBox_p3.addItem("less")

        self.label_p4.setText("修正")
        self.comboBox_p4.addItem("auto")
        self.comboBox_p4.addItem("True")
        self.comboBox_p4.addItem("False")

        self.show_set_parameters(3)
        self.label_s1.setText("变量y")
        self.lineEdit_s1.setEnabled(False)
        self.label_s2.setText("r")
        self.lineEdit_s2.setText("0.707")
        self.label_s3.setText("confidence")
        self.lineEdit_s3.setText("0.95")


    def start_analyse(self):
        self.paras.clear()
        xv = self.listView_1.model().stringList()
        if len(xv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        x = self.dataframe_clumn_2_list(xv)

        if not self.single_y:
            yv = self.listView_2.model().stringList()
            if len(yv) != 1:
                QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
                return
            y = self.dataframe_clumn_2_list(yv)
        else:
            try:
                y = float(self.lineEdit_s1.text())
            except ValueError:
                QMessageBox.warning(None, "参数设置错误", "y需要被设置成float类型的数值。", QMessageBox.Ok)
                return

        self.paras.setdefault("x",x)
        self.paras.setdefault("y",y)

        if self.comboBox_p2.currentIndex() == 0:
            paired = "auto"
        elif self.comboBox_p2.currentIndex() == 1:
            paired = True
        else:
            paired = False
        self.paras.setdefault("paired",paired)
        self.paras.setdefault("alternative",self.comboBox_p3.currentText())
        self.paras.setdefault("correction",self.comboBox_p4.currentText())

        try:
            r = float(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "r需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("r", r)

        try:
            confidence = float(self.lineEdit_s3.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "confidence需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("confidence", confidence)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.ttest, **self.paras)

    def dataframe_clumn_2_list(self, column):
        llist = self.df[column].values.tolist()
        ans = []
        for ll in llist:
            for l in ll:
                ans.append(l)
        return ans

    def adjustY(self):
        index = self.comboBox_p1.currentIndex()
        if index == 0:
            self.single_y = False
            self.listView_2.setEnabled(True)
            self.lineEdit_s1.setEnabled(False)
        else:
            self.single_y = True
            self.listView_2.setEnabled(False)
            self.lineEdit_s1.setEnabled(True)