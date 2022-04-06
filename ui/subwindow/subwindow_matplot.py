#   -*- coding:utf-8 -*-
#   The subwindow_matplot.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 18:48 on 2022/4/6

import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
from ui.subwindow.myqmidsubwindow import MyQMdiSubWindow
from data import Globalvar as gl

class SubWindow_Matplot(MyQMdiSubWindow):
    count = 0
    def __init__(self):
        MyQMdiSubWindow.__init__(self)
        self.win_type = gl.get_value("Window_Matplot")
        SubWindow_Matplot.count += 1
        self.setWindowTitle(self.generate_title(SubWindow_Matplot.count))

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        toolbar = NavigationToolbar(self.canvas, self.window())
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.setWidget(widget)

    def get_canvas(self):
        return self.canvas