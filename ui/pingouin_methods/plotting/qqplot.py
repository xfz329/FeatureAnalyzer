#   -*- coding:utf-8 -*-
#   The qqplot.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 22:51 on 2022/4/9

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin

class Ui_Qqplot_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Generate a Bland-Altman plot to compare two sets of measurements")
        self.url = "https://pingouin-stats.org/generated/pingouin.qqplot.html#pingouin.qqplot"
        self.log.info("qqplot method!")


        self.show_add_parameter(1)
        self.label_l1.setText("x")

        self.show_choose_parameters(0)

        self.show_set_parameters(2)
        self.label_s1.setText("dist")
        self.lineEdit_s1.setText("norm")
        self.label_s2.setText("confidence")
        self.lineEdit_s2.setText("0.95")


    def start_analyse(self):
        paras = {}
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        x = self.df[x[0]]

        # import numpy as np
        # import pingouin as pg
        # np.random.seed(123)
        # x = np.random.normal(size=50)

        paras.setdefault('x',x)
        paras.setdefault("dist",self.lineEdit_s1.text())

        try:
            confidence = float(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "confidence需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("confidence", confidence)

        win = self.win_manager.get_sub_window("Window_Matplot")
        win.get_canvas().figure.clf()
        self.log.info("The Window_Matplot is "+str(win))
        ax = win.get_canvas().figure.subplots()
        paras.setdefault("ax", ax)
        pg.qqplot(**paras)
        win.get_canvas().draw()
        win.get_canvas().flush_events()
        self.info_analyse_finished()

    def info_analyse_finished(self):
        # TODO
        self.log.info("get the answer calculated in the thread")
        ans = self.task.get_ans()
        self.log.info(ans)
        import pandas
        if type(ans) == pandas.core.frame.DataFrame:
            ans.rename(columns=self.columns, inplace=True)
            ans = ans.round(3)
            self.log.info(ans)
        win = self.win_manager.get_sub_window("Window_Result")
        print(win)
        win.setText(str(ans))
