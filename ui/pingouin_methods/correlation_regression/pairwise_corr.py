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
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("(Robust) correlation between two variables")
        self.url = "https://pingouin-stats.org/generated/pingouin.pairwise_corr.html#pingouin.pairwise_corr"
        self.log.info("pairwise_corr method!")

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
        lparas = ()
        # 将 self.df 赋值给lparas 会引起 got multiple values for argument 错误
        paras = {}
        paras.setdefault("data",self.df)
        covar = self.listView_1.model().stringList()
        print(covar)
        paras.setdefault("covar",covar)

        paras.setdefault("alternative",self.comboBox_p1.currentText())

        num = self.comboBox_p2.currentIndex()
        if num > 1:
            QMessageBox.warning(None, "参数设置错误", "该方法还不被Pingouin（0.5.1）支持，请参阅官方文档。",QMessageBox.Ok)
            return
        paras.setdefault("method", self.comboBox_p2.currentText())
        paras.setdefault("padjust", self.comboBox_p3.currentText())
        paras.setdefault("nan_policy", self.comboBox_p4.currentText())

        try:
            columns = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成list类型的数值。该参数设置复杂，建议仔细阅读帮助文件。当前columns已被设置成空list，分析继续。", QMessageBox.Ok)
            columns = None
        if (type(columns) is not list) and (columns is not None):
            QMessageBox.warning(None, "参数设置错误", "kwargs需要被设置成list类型的数值。该参数设置复杂，建议仔细阅读帮助文件。当前columns已被设置成空list，分析继续。", QMessageBox.Ok)
            columns = None
        paras.setdefault("columns",columns)
        self.task.set_worker(pg.pairwise_corr, *lparas, **paras)