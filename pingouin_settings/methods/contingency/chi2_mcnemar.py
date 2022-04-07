#   -*- coding:utf-8 -*-
#   The chi2_mcnemar.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 11:27 on 2022/4/7

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Chi2_mcnemar_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Performs the exact and approximated versions of McNemar’s test")
        self.url = "https://pingouin-stats.org/generated/pingouin.chi2_mcnemar.html#pingouin.chi2_mcnemar"
        self.log.info("chi2_mcnemar method!")


        self.show_add_parameter(2)
        self.label_l1.setText("变量x")
        self.label_l2.setText("变量y")

        self.show_choose_parameters(1)
        self.label_p1.setText("correction")
        self.comboBox_p1.addItem("是")
        self.comboBox_p1.addItem("否")

        self.show_set_parameters(0)

    def start_analyse(self):
        xv = self.listView_1.model().stringList()
        if len(xv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return

        yv = self.listView_2.model().stringList()
        if len(yv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        lparas = (self.df,xv[0],yv[0])
        paras = {}
        paras.setdefault("correction",self.comboBox_p1.currentIndex()==0)

        self.task.set_worker(pg.chi2_mcnemar, *lparas, **paras)