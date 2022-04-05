#   -*- coding:utf-8 -*-
#   The ancova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 1:49 on 2022/4/5
from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow


class Ui_Ancova_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("ANCOVA with one or more covariate(s)")
        self.url = "https://pingouin-stats.org/generated/pingouin.ancova.html#pingouin.ancova"

        self.show_add_parameter(3)
        self.label_l1.setText("独立变量")
        self.label_l2.setText("检测变量")
        self.label_l3.setText("协变量")

        self.show_choose_parameters(1)
        self.label_p1.setText("效应值")
        self.comboBox_p1.addItem("偏η2")
        self.comboBox_p1.addItem("η2")

        self.show_set_parameters(0)


    def start_analyse(self):
        self.log.info("empty method!")
        paras = {}
        paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "独立变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("dv",dv[0])
        between = self.listView_2.model().stringList()
        if len(between) != 1:
            QMessageBox.warning(None, "参数设置错误", "检测变量能且只能设置一个。",QMessageBox.Ok)
            return
        paras.setdefault("between",between[0])
        covar = self.listView_3.model().stringList()
        if len(covar) == 0:
            QMessageBox.warning(None, "参数设置错误", "至少需要设置一个协变量。",QMessageBox.Ok)
            return
        paras.setdefault("covar", covar)
        if self.comboBox_p1.currentIndex() == 0:
            effsize = "np2"
        else:
            effsize ="n2"
        paras.setdefault("effsize",effsize)

        for key in paras.keys():
            if key != "data":
                print(key)
                print(paras[key])
        self.task.set_worker(pg.ancova, **paras)
        # self.task.set_worker(pg.anova, dv='Pain threshold', between='Hair color', data=self.df, detailed=True)

    def info_analyse_finished(self):
        self.log.info("get the answer calculated in the thread")
        ans = self.task.get_ans()
        self.log.info(ans)
        ans.rename(columns=self.columns, inplace=True)
        self.log.info(ans)
        win = self.win_manager.get_sub_window("Window_Result")
        win.setText(str(ans))