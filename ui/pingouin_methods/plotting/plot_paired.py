#   -*- coding:utf-8 -*-
#   The plot_paired.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:24 on 2022/4/9

import os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime

import pingouin as pg
from ui.pingouin_methods import SubWindow_Pingouin
import data.Globalvar as gl

class Ui_Plot_paired_MainWindow(SubWindow_Pingouin):
    def __init__(self):
        SubWindow_Pingouin.__init__(self)
        self.set_widgets()
        self.set_widgets()

    def set_widgets(self):
        self.label_method.setText("Paired plot")
        self.url = "https://pingouin-stats.org/generated/pingouin.plot_paired.html#pingouin.plot_paired"
        self.log.info("plot_paired method!")

        self.desc.setdefault("detail", "Paired plot")
        self.desc.setdefault("brief", "plot_paired method!")
        self.desc.setdefault("url", self.url)


        self.show_add_parameter(3)
        self.label_l1.setText("dv")
        self.label_l2.setText("within")
        self.label_l3.setText("subject")

        self.show_choose_parameters(3)
        self.label_p1.setText("boxplot")
        self.comboBox_p1.addItem("True")
        self.comboBox_p1.addItem("False")
        self.label_p2.setText("boxplot_in_front")
        self.comboBox_p2.addItem("False")
        self.comboBox_p2.addItem("True")
        self.label_p3.setText("orient")
        self.comboBox_p3.addItem("v")
        self.comboBox_p3.addItem("h")

        self.show_set_parameters(4)
        self.label_s1.setText("dpi")
        self.lineEdit_s1.setText("100")
        self.label_s2.setText("colors")
        self.lineEdit_s2.setText("['green','grey','indianred']")
        self.label_s3.setText("pointplot_kwargs")
        self.lineEdit_s3.setText("{'marker': '.', 'scale': 0.6}")
        self.label_s4.setText("boxplot_kwargs")
        self.lineEdit_s4.setText("{'color': 'lightslategrey','width':0.2}")

    def start_analyse(self):
        self.paras.clear()
        self.paras.setdefault("data",self.df)
        dv = self.listView_1.model().stringList()
        if len(dv) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量dv能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("dv",dv[0])

        within = self.listView_2.model().stringList()
        if len(within) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量within能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("within", within[0])

        subject = self.listView_3.model().stringList()
        if len(subject) != 1:
            QMessageBox.warning(None, "参数设置错误", "变量subject能且只能设置一个。", QMessageBox.Ok)
            return
        self.paras.setdefault("subject", subject[0])

        self.paras.setdefault("order",None)
        self.paras.setdefault("boxplot",self.comboBox_p1.currentIndex()==0)
        self.paras.setdefault("boxplot_in_front",self.comboBox_p2.currentIndex()==0)
        self.paras.setdefault("orient",self.comboBox_p3.currentText())

        try:
            dpi = int(self.lineEdit_s1.text())
        except ValueError:
            QMessageBox.warning(None, "参数设置错误", "dpi需要被设置成int类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("dpi", dpi)


        try:
            colors = eval(self.lineEdit_s2.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "colors需要被设置成list类型的数值。", QMessageBox.Ok)
            return
        if type(colors) is not list:
            QMessageBox.warning(None, "参数设置错误", "colors需要被设置成list类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("colors", colors)

        try:
            pointplot_kwargs = eval(self.lineEdit_s3.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "pointplot_kwargs需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        if type(pointplot_kwargs) is not dict:
            QMessageBox.warning(None, "参数设置错误", "pointplot_kwargs需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("pointplot_kwargs", pointplot_kwargs)

        try:
            boxplot_kwargs = eval(self.lineEdit_s4.text())
        except Exception:
            QMessageBox.warning(None, "参数设置错误", "boxplot_kwargs需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        if type(boxplot_kwargs) is not dict:
            QMessageBox.warning(None, "参数设置错误", "boxplot_kwargs需要被设置成dict类型的数值。", QMessageBox.Ok)
            return
        self.paras.setdefault("boxplot_kwargs", boxplot_kwargs)

        win = gl.get_value("Win_manager").get_sub_window("Window_Matplot")
        win.get_canvas().figure.clf()
        self.log.info("The Window_Matplot is " + str(win))
        ax = win.get_canvas().figure.subplots()
        self.paras.setdefault("ax", ax)
        self.desc["start_time"] = QDateTime.currentDateTime().toString("HH:mm:ss.zzz")
        pg.plot_paired(**self.paras)
        win.get_canvas().draw()
        win.get_canvas().flush_events()
        name = "Fig_" + QDateTime.currentDateTime().toString("yyMMdd_HHmmss") + ".jpg"
        full_name = os.path.join(gl.get_value("FIG_PATH"), name)
        win.get_canvas().figure.savefig(full_name)
        self.desc['path'] = full_name
        self.info_draw_finished()