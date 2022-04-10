#   -*- coding:utf-8 -*-
#   The plot_rm_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 23:25 on 2022/4/9

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin

class Ui_Plot_rm_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Plot a repeated measures correlation")
        self.url = "https://pingouin-stats.org/generated/pingouin.plot_paired.html#pingouin.plot_paired"
        self.log.info("plot_rm_corr method!")

        self.show_add_parameter(3)
        self.label_l1.setText("x")
        self.label_l2.setText("y")
        self.label_l3.setText("subject")

        self.show_choose_parameters(1)
        self.label_p1.setText("legend")
        self.comboBox_p1.addItem("False")
        self.comboBox_p1.addItem("True")

        self.show_set_parameters(1)
        self.label_s1.setText("kwargs_facetgrid")
        self.lineEdit_s1.setText("{'aspect': 1,'height':4}")

    def start_analyse(self):
        paras = {}
        paras.setdefault("data",self.df)
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("x",x[0])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("y", y[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("subject", subject[0])
        paras.setdefault("legend",self.comboBox_p1.currentIndex()==1)

        try:
            kwargs_facetgrid = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "kwargs_facetgrid需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        if type(kwargs_facetgrid) is not dict:
            QMessageBox.warning(None, "参数设置错误", "kwargs_facetgrid需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("kwargs_facetgrid", kwargs_facetgrid)

        g = pg.plot_rm_corr(**paras)
        win = self.win_manager.get_sub_window("Window_Matplot")
        self.log.info("The Window_Matplot is " + str(win))
        win.reset_canvas(g.fig)
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