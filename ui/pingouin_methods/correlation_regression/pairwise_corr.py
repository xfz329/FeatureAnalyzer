#   -*- coding:utf-8 -*-
#   The pairwise_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:23 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin


class Ui_Pairwise_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("(Robust) correlation between two variables")
        self.url = "https://pingouin-stats.org/generated/pingouin.pairwise_corr.html#pingouin.pairwise_corr"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "pairwise_corr method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

        self.show_add_parameter(1)
        self.label_l1.setText("covar")

        self.show_choose_parameters(4)
        self.label_p1.setText("alternative")
        self.comboBox_p1.addItem("two-sided")
        self.comboBox_p1.addItem("greater")
        self.comboBox_p1.addItem("less")


        self.label_p2.setText("method")
        self.comboBox_p2.addItem("pearson")
        self.comboBox_p2.addItem("spearman")
        self.comboBox_p2.addItem("kendall")
        self.comboBox_p2.addItem("bicor")
        self.comboBox_p2.addItem("percbend")
        self.comboBox_p2.addItem("shepherd")
        self.comboBox_p2.addItem("skipped")

        self.label_p3.setText("padjust")
        self.comboBox_p3.addItem("none")
        self.comboBox_p3.addItem("bonf")
        self.comboBox_p3.addItem("sidak")
        self.comboBox_p3.addItem("holm")
        self.comboBox_p3.addItem("fdr_bh")
        self.comboBox_p3.addItem("fdr_by")

        self.label_p4.setText("nan_policy")
        self.comboBox_p4.addItem("pairwise")
        self.comboBox_p4.addItem("listwise")

        self.show_set_parameters(1)
        self.label_s1.setText("columns")
        self.lineEdit_s1.setText("None")

    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)
        covar = self.listView_1.model().stringList()
        if len(covar) == 0:
            covar = None
        self.paras.setdefault("covar",covar)

        self.paras.setdefault("alternative",self.comboBox_p1.currentText())

        num = self.comboBox_p2.currentIndex()
        if covar is not None and num > 1:
            QMessageBox.warning(None, "??????????????????", "covar ??????None???????????????pearson???spearman?????????",QMessageBox.Ok)
            return
        self.paras.setdefault("method", self.comboBox_p2.currentText())
        self.paras.setdefault("padjust", self.comboBox_p3.currentText())
        self.paras.setdefault("nan_policy", self.comboBox_p4.currentText())

        try:
            columns = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "??????????????????", "kwargs??????????????????list?????????????????????????????????????????????????????????????????????????????????columns??????????????????list??????????????????", QMessageBox.Ok)
            columns = None
        if (type(columns) is not list) and (columns is not None):
            QMessageBox.warning(None, "??????????????????", "kwargs??????????????????list?????????????????????????????????????????????????????????????????????????????????columns??????????????????list??????????????????", QMessageBox.Ok)
            columns = None
        self.paras.setdefault("columns",columns)

        from PyQt5.QtCore import QDateTime
        self.desc["start_time"] = QDateTime.currentDateTime()
        self.task.set_worker(pg.pairwise_corr, **self.paras)