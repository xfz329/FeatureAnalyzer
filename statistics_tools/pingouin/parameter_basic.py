# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter_basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 54, 12))
        self.label_3.setObjectName("label_3")
        self.comboBox_Subwindow = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Subwindow.setGeometry(QtCore.QRect(230, 110, 181, 22))
        self.comboBox_Subwindow.setObjectName("comboBox_Subwindow")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "统计参数设置"))
        self.label.setText(_translate("MainWindow", "数据源设置"))
        self.label_2.setText(_translate("MainWindow", "数据窗口选择"))
        self.label_3.setText(_translate("MainWindow", "数据项设置"))
