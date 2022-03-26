# mainWindow.py
import math
import sys
import time
from random import randint, random

import numpy as np

from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, QObject, Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
                             QMainWindow, QVBoxLayout, QWidget)

from QCustomPlot2 import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1283, 889)
        Form.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(460, 100, 496, 36))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.log = QtWidgets.QLabel(Form)
        self.log.setGeometry(QtCore.QRect(210, 60, 151, 151))
        self.log.setText("")
        self.log.setPixmap(QtGui.QPixmap("F:/图片/保存的图片/科大校徽1.jpg"))
        self.log.setScaledContents(True)
        self.log.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.log.setObjectName("log")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(460, 220, 511, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.linechart = QCustomPlot(self.layoutWidget)
        self.linechart.setObjectName("linechart")
        self.verticalLayout.addWidget(self.linechart)
        self.fallchart = QCustomPlot(self.layoutWidget)
        self.fallchart.setObjectName("fallchart")
        self.verticalLayout.addWidget(self.fallchart)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 360, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate(
            "Form", "Deep Learning Signal Classifier"))
        self.pushButton.setText(_translate("Form", "开始采集"))
        self.pushButton_2.setText(_translate("Form", "单次调试"))

class MainWidow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWidow, self).__init__()
        self.setupUi(self)          # setupUi方法写在Ui_Form类中

        self.pushButton.clicked.connect(self.waveplot)
        self.pushButton_2.clicked.connect(self.waterfall)

        self.timer = QTimer()       # 定义计时器
        self.timer.timeout.connect(self.waterfall)
        self.is_running = False
        self.log_value = []

    '''方法实现区'''

    def waveplot(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
        else:
            self.timer.start(200)
            self.is_running = True

    def waterfall(self):
        customPlot = self.fallchart
        self.colorMap = QCPColorMap(customPlot.xAxis, customPlot.yAxis)
        self.colorMap.data().setSize(200, 50)
        self.colorMap.data().setRange(QCPRange(0, 1024), QCPRange(0, 100))

        self.log_value.insert(0, np.random.randint(
            0, 255, 200))   # 随即生成新的随机向量模拟新到来数据
        if len(self.log_value) > 50:
            # 只缓存最新的50条数据
            self.log_value.pop()

        for i in range(len(self.log_value)):
            row_vec = self.log_value[i]
            for j in range(row_vec.size):
                self.colorMap.data().setCell(
                    j, 49-i, row_vec[j])  # 根据生成的数据，逐个单元调整颜色深度
        self.colorMap.rescaleDataRange(True)
        customPlot.rescaleAxes()
        customPlot.replot()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = MainWidow()
    form.show()
    sys.exit(app.exec_())

