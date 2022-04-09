#   -*- coding:utf-8 -*-
#   The subwindow_matplot.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 18:48 on 2022/4/6

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
        self.layout = QtWidgets.QVBoxLayout(widget)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas.figure.subplots()
        self.canvas.mpl_connect('scroll_event', self.call_back_scroll)
        self.toolbar = NavigationToolbar(self.canvas, self.window())
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setWidget(widget)

    def get_canvas(self):
        return self.canvas

    def reset_canvas(self,fig, keep_toolbar = False):
        self.layout.removeWidget(self.canvas)
        if not keep_toolbar:
            self.layout.removeWidget(self.toolbar)
        self.canvas = FigureCanvas(fig)
        self.layout.addWidget(self.canvas)

    def call_back_scroll(self,event):
        ax = event.inaxes
        if ax is not None:
            ax = event.inaxes
            x_min, x_max = ax.get_xlim()
            xrange = (x_max - x_min) / 10
            if event.button == 'up':
                ax.set(xlim=(x_min + xrange, x_max - xrange))
                print('up')
            elif event.button == 'down':
                ax.set(xlim=(x_min - xrange, x_max + xrange))
                print('down')
            self.get_canvas().draw_idle()