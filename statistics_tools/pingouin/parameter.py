#   -*- coding:utf-8 -*-
#   The parameter.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:31 on 2022/3/31

from PyQt5 import QtCore, QtGui, QtWidgets
from statistics_tools.pingouin.parameter_basic import  Ui_MainWindow
from data import Globalvar as gl
from ui.subwindow.SubWindow import SubwindowManager


class Ui_Parameter_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Ui_Parameter_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.comboBox_Subwindow.addItem("")
        for key in gl.get_dict():
            if key.startswith(SubwindowManager.Key_Window_Data+'-'):
                self.comboBox_Subwindow.addItem(key)
                print(key)
        self.comboBox_Subwindow.activated.connect(self.load_data)

    def load_data(self):
        from PyQt5.QtWidgets import QMessageBox
        if self.comboBox_Subwindow.currentText() != "":
            QMessageBox.information(None, "载入数据","获取 "+self.comboBox_Subwindow.currentText()+ " 中的内容成功",QMessageBox.Ok)


