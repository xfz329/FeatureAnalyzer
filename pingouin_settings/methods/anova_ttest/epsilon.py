#   -*- coding:utf-8 -*-
#   The epsilon.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 14:33 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Epsilon_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Epsilon adjustement factor for repeated measures")
        self.url = "https://pingouin-stats.org/generated/pingouin.epsilon.html#pingouin.epsilon"
        self.log.info("epsilon method!")

        self.show_add_parameter(3)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("within")
        self.label_l3.setText("subject")

        self.show_choose_parameters(1)
        self.label_p1.setText("修正")
        self.comboBox_p1.addItem("gg")
        self.comboBox_p1.addItem("hf")
        self.comboBox_p1.addItem("lb")
        self.show_set_parameters(0)


    def start_analyse(self):
        paras = {}
        paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "独立变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("dv",dv[0])
        within = self.listView_2.model().stringList()
        if len(within) == 1:
            paras.setdefault("within", within[0])
        elif len(within) == 2:
            paras.setdefault("within", within)
        else:
            QMessageBox.warning(None, "参数设置错误", "with变量只能设置为一个或两个。",QMessageBox.Ok)
            return
        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "subject变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])

        if self.comboBox_p1.currentIndex() == 0:
            correction = "gg"
        elif self.comboBox_p1.currentIndex() == 1:
            correction = "hf"
        else:
            correction ="lb"
        paras.setdefault("correction",correction)

        self.task.set_worker(pg.epsilon, **paras)