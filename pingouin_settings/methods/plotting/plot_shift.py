#   -*- coding:utf-8 -*-
#   The plot_shift.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 21:50 on 2022/4/9
from PyQt5.QtWidgets import QMessageBox

import pingouin as pg
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow

class Ui_Plot_shift_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Shift plot")
        self.url = "https://pingouin-stats.org/generated/pingouin.plot_shift.html#pingouin.plot_shift"
        self.log.info("plot_shift method!")


        self.show_add_parameter(2)
        self.label_l1.setText("x")
        self.label_l2.setText("y")

        self.show_choose_parameters(3)
        self.label_p1.setText("paired")
        self.comboBox_p1.addItem("True")
        self.comboBox_p1.addItem("False")
        self.label_p2.setText("show_median")
        self.comboBox_p2.addItem("True")
        self.comboBox_p2.addItem("False")
        self.label_p3.setText("violin")
        self.comboBox_p3.addItem("True")
        self.comboBox_p3.addItem("False")

        self.show_set_parameters(4)
        self.label_s1.setText("n_boot")
        self.lineEdit_s1.setText("1000")
        self.label_s2.setText("percentiles")
        self.lineEdit_s2.setText(" [10, 20, 30, 40, 50, 60, 70, 80, 90]")
        self.label_s3.setText("ci")
        self.lineEdit_s3.setText("0.95")
        self.label_s4.setText("seed")
        self.lineEdit_s4.setText("None")


    def start_analyse(self):
        paras = {}
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("x",self.df[x[0]])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        paras.setdefault("y", self.df[y[0]])

        paras.setdefault("paired",self.comboBox_p1.currentIndex()==0)
        paras.setdefault("show_median",self.comboBox_p2.currentIndex()==0)
        paras.setdefault("violin",self.comboBox_p3.currentIndex()==0)

        try:
            n_boot = int(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "n_boot需要被设置成int类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("n_boot", n_boot)

        try:
            percentiles = eval(self.lineEdit_s2.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "percentiles需要被设置成list类型的数值。", QMessageBox.Ok)
            return
        if type(percentiles) is not list:
            QMessageBox.warning(None, "参数设置错误", "percentiles需要被设置成list类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("percentiles", percentiles)

        try:
            ci = float(self.lineEdit_s3.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "ci需要被设置成float类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("ci", ci)

        try:
            seed = eval(self.lineEdit_s4.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "seed需要被设置成None或int类型的数值。", QMessageBox.Ok)
            return
        if seed is not None:
            if type(seed) is not int:
                QMessageBox.warning(None, "参数设置错误", "seed需要被设置成None或int类型的数值。", QMessageBox.Ok)
            return
        paras.setdefault("seed", seed)

        # import numpy as np
        # import pingouin as pg
        # np.random.seed(42)
        # x = np.random.normal(5.5, 2, 50)
        # y = np.random.normal(6, 1.5, 50)
        # paras.setdefault("x", x)
        # paras.setdefault("y", y)
        fig = pg.plot_shift(**paras)

        win = self.win_manager.get_sub_window("Window_Matplot")
        self.log.info("The Window_Matplot is " + str(win))
        win.reset_canvas(fig)
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