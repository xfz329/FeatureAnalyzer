#   -*- coding:utf-8 -*-
#   The plot_rm_corr.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 23:25 on 2022/4/9

import os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin
import data.Globalvar as gl

class Ui_Plot_rm_corr_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Plot a repeated measures correlation")
        self.url = "https://pingouin-stats.org/generated/pingouin.plot_paired.html#pingouin.plot_paired"
        self.desc.setdefault("detail", self.label_method.text())
        self.desc.setdefault("brief", "plot_rm_corr method!")
        self.desc.setdefault("url", self.url)
        self.log.info(self.desc["brief"])

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
        self.paras.clear()
        self.paras.setdefault("data",self.df)
        x = self.listView_1.model().stringList()
        if len(x) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量x能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("x",x[0])

        y = self.listView_2.model().stringList()
        if len(y) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量y能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("y", y[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("subject", subject[0])
        self.paras.setdefault("legend",self.comboBox_p1.currentIndex()==1)

        try:
            kwargs_facetgrid = eval(self.lineEdit_s1.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "kwargs_facetgrid需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        if type(kwargs_facetgrid) is not dict:
            QMessageBox.warning(None, "参数设置错误", "kwargs_facetgrid需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("kwargs_facetgrid", kwargs_facetgrid)
        self.desc["start_time"] = QDateTime.currentDateTime()

        import traceback
        try:
            g = pg.plot_rm_corr(**self.paras)
        except Exception as e:
            self.log.error(e)
            info = traceback.format_exc()
            self.log.error(info)
            QMessageBox.warning(None, "参数错误","程序运行出错！以下是错误信息，请检查！\n\t错误类型 : " + str(e) + "\n\t 错误堆栈 : " + info,QMessageBox.Ok)
            return
        win = gl.get_value("Win_manager").get_sub_window("Window_Matplot")
        self.log.info("The Window_Matplot is " + str(win))
        win.reset_canvas(g.fig)
        name = "Fig_" + QDateTime.currentDateTime().toString("yyMMdd_HHmmss") + ".jpg"
        full_name = os.path.join(gl.get_value("FIG_PATH"), name)
        win.get_canvas().figure.savefig(full_name)
        self.desc['path'] = full_name
        self.info_draw_finished()