#   -*- coding:utf-8 -*-
#   The subwindow_qcustomplot.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 18:26 on 2022/3/31

from PyQt5 import QtCore,QtWidgets
from QCustomPlot2 import *
from ui.subwindow.myqmidsubwindow import MyQMdiSubWindow
from data import Globalvar as gl

class SubWindow_QCustomPlot(MyQMdiSubWindow):
    count = 0
    def __init__(self):
        MyQMdiSubWindow.__init__(self)
        self.win_type = gl.get_value("Window_Plot")
        # 与其他三个子类不同，必须设置成False, 否则关闭绘图窗口会直接导致程序退出
        # 未知bug？
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, False)
        SubWindow_QCustomPlot.count += 1
        self.setWindowTitle(self.generate_title(SubWindow_QCustomPlot.count))

        widget = QtWidgets.QWidget()
        plot = QCustomPlot(widget)
        plot.mousePress.connect(self.mousePress)
        plot.mouseWheel.connect(self.mouseWheel)
        self.setWidget(plot)

    def mousePress(self):
        plot = self.widget()
        if type(plot).__name__ != 'QCustomPlot':
            self.log.error("It's not a drawing sub win")
            return
        if plot.xAxis.selectedParts() == QCPAxis.SelectablePart.spAxis:
            plot.axisRect().setRangeDrag(plot.xAxis.orientation())
        elif plot.yAxis.selectedParts() == QCPAxis.SelectablePart.spAxis:
            plot.axisRect().setRangeDrag(plot.yAxis.orientation())
        else:
            plot.axisRect().setRangeDrag(QtCore.Qt.Orientation.Horizontal | QtCore.Qt.Orientation.Vertical)

    def mouseWheel(self):
        plot = self.widget()
        if type(plot).__name__ != 'QCustomPlot':
            self.log.error("It's not a drawing sub win")
            return
        if plot.xAxis.selectedParts() == QCPAxis.SelectablePart.spAxis:
            plot.axisRect().setRangeZoom(plot.xAxis.orientation())
        elif plot.yAxis.selectedParts() == QCPAxis.SelectablePart.spAxis:
            plot.axisRect().setRangeZoom(plot.yAxis.orientation())
        else:
            plot.axisRect().setRangeZoom(QtCore.Qt.Orientation.Horizontal | QtCore.Qt.Orientation.Vertical)