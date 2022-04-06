#   -*- coding:utf-8 -*-
#   The ttest.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:55 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Ttest_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.single_y = False
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("T-test")
        self.url = "https://pingouin-stats.org/generated/pingouin.ttest.html#pingouin.ttest"
        self.log.info("ttest method!")


        self.show_add_parameter(2)
        self.label_l1.setText("变量x")
        self.label_l2.setText("变量y")

        self.show_choose_parameters(4)
        self.label_p1.setText("y变量数据类型")
        self.comboBox_p1.addItem("列表")
        self.comboBox_p1.addItem("单值")
        self.comboBox_p1.currentIndexChanged.connect(self.adjustY)

        self.label_p2.setText("paired")
        self.comboBox_p2.addItem("否")
        self.comboBox_p2.addItem("是")

        self.label_p3.setText("alternative")
        self.comboBox_p3.addItem("two-sided")
        self.comboBox_p3.addItem("greater")
        self.comboBox_p3.addItem("less")

        self.label_p4.setText("修正")
        self.comboBox_p4.addItem("auto")
        self.comboBox_p4.addItem("是")
        self.comboBox_p4.addItem("否")

        self.show_set_parameters(3)
        self.label_s1.setText("变量y")
        self.lineEdit_s1.setEnabled(False)
        self.label_s2.setText("r")
        self.lineEdit_s2.setText("0.707")
        self.label_s3.setText("confidence")
        self.lineEdit_s3.setText("0.95")


    def start_analyse(self):
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

        lparas = (x,y)
        paras = {}

        if self.comboBox_p2.currentIndex() == 0:
            paired = "auto"
        elif self.comboBox_p2.currentIndex() == 1:
            paired = True
        else:
            paired = False
        paras.setdefault("paired",paired)

        if self.comboBox_p3.currentIndex() == 0:
            alternative = "two-sided"
        elif self.comboBox_p3.currentIndex() == 1:
            alternative = "greater"
        else:
            alternative = "less"
        paras.setdefault("alternative",alternative)

        try:
            r = float(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "r需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("r", r)

        try:
            confidence = float(self.lineEdit_s3.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "confidence需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("confidence", confidence)

        self.task.set_worker(pg.ttest, *lparas, **paras)

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