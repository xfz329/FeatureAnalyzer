#   -*- coding:utf-8 -*-
#   The plot_blandaltman.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:25 on 2022/4/6

from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin

class Ui_Plot_blandaltman_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Generate a Bland-Altman plot to compare two sets of measurements")
        self.url = "https://pingouin-stats.org/generated/pingouin.plot_blandaltman.html#pingouin.plot_blandaltman"
        self.log.info("plot_blandaltman method!")


        self.show_add_parameter(2)
        self.label_l1.setText("变量x")
        self.label_l2.setText("变量y")

        self.show_choose_parameters(2)
        self.label_p1.setText("xaxis")
        self.comboBox_p1.addItem("mean")
        self.comboBox_p1.addItem("x")
        self.comboBox_p1.addItem("y")
        self.label_p2.setText("annotate")
        self.comboBox_p2.addItem("是")
        self.comboBox_p2.addItem("否")

        self.show_set_parameters(4)
        self.label_s1.setText("agreement")
        self.lineEdit_s1.setText("1.96")
        self.label_s2.setText("confidence")
        self.lineEdit_s2.setText("0.95")
        self.label_s3.setText("scatter_kws")
        self.lineEdit_s3.setText("{'alpha': 0.8, 'color': 'tab:blue'}")
        self.label_s4.setText("dpi")
        self.lineEdit_s4.setText("100")


    def start_analyse(self):
        xv = self.listView_1.model().stringList()
        if len(xv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        x = self.df[xv[0]]

        yv = self.listView_2.model().stringList()
        if len(yv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        y = self.df[yv[0]]
        lparas = (x, y)
        paras = {}

        if self.comboBox_p1.currentIndex() == 0:
            xaxis = "mean"
        elif self.comboBox_p1.currentIndex() == 1:
            xaxis = "x"
        else:
            xaxis = "y"
        paras.setdefault("xaxis", xaxis)
        paras.setdefault("annotate", self.comboBox_p2.currentIndex() == 0)

        try:
            agreement = float(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "agreement需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("agreement", agreement)

        try:
            confidence = float(self.lineEdit_s2.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "confidence需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("confidence", confidence)

        try:
            scatter_kws = eval(self.lineEdit_s3.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "scatter_kws需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        if type(scatter_kws) is not dict:
            QMessageBox.warning(None, "参数设置错误", "scatter_kws需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("scatter_kws", scatter_kws)

        try:
            dpi = int(self.lineEdit_s4.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "dpi需要被设置成int类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("dpi", dpi)
        win = self.win_manager.get_sub_window("Window_Matplot")
        win.get_canvas().figure.clf()
        self.log.info("The Window_Matplot is "+str(win))
        ax = win.get_canvas().figure.subplots()
        paras.setdefault("ax", ax)
        pg.plot_blandaltman(*lparas, **paras)
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
