#   -*- coding:utf-8 -*-
#   The Draw.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:44 on 2022/3/29

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtWidgets import QMessageBox
from QCustomPlot2 import *
from utils.logger import Logger

class Draw:

    def __init__(self):
        self.log = Logger("fa").get_log()
        self.x = []
        self.y = []

    def check_data(self,data):
        if data.widget().model().dataFrame().empty:
            QMessageBox.warning(None, '警告', '当前数据窗口('+data.windowTitle()+')无数据可供绘制', QMessageBox.Ok)
            return False
        index = data.widget().tableView.selectedIndexes()
        if len(index) == 0:
            QMessageBox.warning(None, '警告', '当前数据窗口('+data.windowTitle()+')没有任何数据被选中！', QMessageBox.Ok)
            return False
        return True

    def prepare_data(self,data):
        index = data.widget().tableView.selectedIndexes()
        row_dict = {}
        for ix in index:
            row_dict[str(ix.column())]=ix.column()
            # print(ix.row(), ix.column())
        rows = list(row_dict.values())
        self.log.info("The selected column are "+str(rows))

        df = data.widget().model().dataFrame()

        if len(row_dict) == 2 :
            # self.x = df.iloc[:,[rows[0]]]
            # self.y = df.iloc[:, [rows[1]]
            # print(self.x,self.y)
            return True
        if len(row_dict) == 1:
            # self.x = df.iloc[:, [rows[0]]]
            line = rows[0]
            self.y = df.iloc[:, line].tolist()
            self.x = list(range(len(self.y)))

            print(type(self.y))
            print(type(self.x))
            return True
        else:
            return False

    def start_plot(self,plot):

        customPlot = plot.widget()

        customPlot.clearGraphs()

        graph0 = customPlot.addGraph()
        graph0.setPen(QPen(Qt.blue))
        graph0.setBrush(QBrush(QColor(0, 0, 255, 20)))

        graph0.setData(self.x, self.y)

        customPlot.rescaleAxes()
        customPlot.setInteraction(QCP.iRangeDrag)
        customPlot.setInteraction(QCP.iRangeZoom)
        customPlot.setInteraction(QCP.iSelectPlottables)
        customPlot.replot()

    def draw(self, data, plot):
        if not self.check_data(data):
            return False
        if self.prepare_data(data):
            self.start_plot(plot)

