#   -*- coding:utf-8 -*-
#   The SubWindow.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:07 on 2022/3/29
from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QMdiArea,QMdiSubWindow,QWidget, QVBoxLayout,QHBoxLayout,QFormLayout
from QCustomPlot2 import *
import data.Globalvar as gl
from utils.logger import Logger
from ui.subwindow.title import Title

class SubwindowManager(object):
    Window_Data          =    0x0001
    Window_Plot          =    0x0010
    Window_Logs          =    0x0100
    Window_Result       =    0x1000

    Key_Window_Data         =   "数据窗口"
    Key_Window_Plot         =   "绘图窗口"
    Key_Window_Logs         =   "日志窗口"
    Key_Window_Result       =   "输出窗口"

    default_width  =    800
    default_height =    600

    def __init__(self,area):
        t_data = Title(SubwindowManager.Window_Data,SubwindowManager.Key_Window_Data)
        t_plot = Title(SubwindowManager.Window_Plot, SubwindowManager.Key_Window_Plot)
        t_logs = Title(SubwindowManager.Window_Logs, SubwindowManager.Key_Window_Logs)
        t_result = Title(SubwindowManager.Window_Result, SubwindowManager.Key_Window_Result)
        self.titles=[t_data,t_plot,t_logs,t_result]
        self.mdi_area = area
        self.log = Logger("fa").get_log()
        self.mdi_area.subWindowActivated.connect(self.update_actived_window)


    def add_sub_window_data(self):
        from qtpandas.views.DataTableView import DataTableWidget
        from qtpandas.models.DataFrameModel import DataFrameModel

        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Data)
        sub.setWindowTitle(title[0])
        sub.resize(SubwindowManager.default_width, SubwindowManager.default_height)
        # 在子窗口中添加一个标签，并设置文本
        widget = DataTableWidget()
        widget.tableView.setSortingEnabled(False)
        model = DataFrameModel()
        widget.setViewModel(model)
        sub.setWidget(widget)
        self.save_sub_window(title, sub)
        self.mdi_area.addSubWindow(sub)  # 将新建的子窗口添加到MDI区域
        sub.signal_close.connect(self.update_closed_window)
        sub.show()

    def add_sub_window_plot(self):

        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Plot)
        sub.setWindowTitle(title[0])
        sub.resize(SubwindowManager.default_width, SubwindowManager.default_height)
        widget = QtWidgets.QWidget()
        plot = QCustomPlot(widget)
        sub.setWidget(plot)
        self.save_sub_window(title, sub)
        self.mdi_area.addSubWindow(sub)
        sub.signal_close.connect(self.update_closed_window)
        sub.show()

    def add_sub_window_logs(self):
        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Logs)
        sub.setWindowTitle(title[0])
        sub.resize(SubwindowManager.default_width,SubwindowManager.default_height)

        centralwidget = QtWidgets.QWidget()

        scrollArea = QtWidgets.QScrollArea(centralwidget)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, SubwindowManager.default_width-20, SubwindowManager.default_height-20))
        scrollArea.setWidget(scrollAreaWidgetContents)

        label = QtWidgets.QLabel(scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)

        from help.changelogs.changelogs_template import Template
        label.setText(Template().get())

        formLayout = QtWidgets.QFormLayout(scrollAreaWidgetContents)
        formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)

        formLayout_2 = QtWidgets.QFormLayout(centralwidget)
        formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, scrollArea)

        sub.setWidget(centralwidget)
        self.save_sub_window(title, sub)
        self.mdi_area.addSubWindow(sub)
        sub.signal_close.connect(self.update_closed_window)
        sub.show()


    def add_sub_window_result(self):
        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Result)
        sub.setWindowTitle(title[0])
        sub.resize(SubwindowManager.default_width, SubwindowManager.default_height)

        centralwidget = QtWidgets.QWidget()

        scrollArea = QtWidgets.QScrollArea(centralwidget)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, SubwindowManager.default_width-20, SubwindowManager.default_height-20))
        scrollArea.setWidget(scrollAreaWidgetContents)

        label = QtWidgets.QLabel(scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)

        from help.changelogs.changelogs_template import Template
        label.setText(Template().get())

        formLayout = QtWidgets.QFormLayout(scrollAreaWidgetContents)
        formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)

        formLayout_2 = QtWidgets.QFormLayout(centralwidget)
        formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, scrollArea)

        sub.setWidget(centralwidget)
        self.save_sub_window(title, sub)
        self.mdi_area.addSubWindow(sub)
        sub.signal_close.connect(self.update_closed_window)
        sub.show()

    def save_sub_window(self,title,win):
        gl.set_value(title[0] , win)
        gl.set_value(title[1], win)


    def get_sub_window_data(self):
        if gl.get_value(SubwindowManager.Key_Window_Data)is None:
            self.log.warning("尚无数据窗口，开始创建新的数据窗口")
            self.add_sub_window_data()
        return gl.get_value(SubwindowManager.Key_Window_Data)

    def get_sub_window_plot(self):
        if gl.get_value(SubwindowManager.Key_Window_Plot) is None:
            self.log.warning("尚无绘图窗口，开始创建新的绘图窗口")
            self.add_sub_window_plot()
        return gl.get_value(SubwindowManager.Key_Window_Plot)

    def get_sub_window_logs(self):
        if gl.get_value(SubwindowManager.Key_Window_Logs) is None:
            self.log.warning("尚无日志窗口，开始创建新的日志窗口")
            self.add_sub_window_logs()
        return gl.get_value(SubwindowManager.Key_Window_Logs)

    def get_sub_window_result(self):
        if gl.get_value(SubwindowManager.Key_Window_Result) is None:
            self.log.warning("尚无输出窗口，开始创建新的输出窗口")
            self.add_sub_window_result()
        return gl.get_value(SubwindowManager.Key_Window_Result)

    def generate_win_title(self, wintype):
        for t in self.titles:
            if t.is_winType(wintype):
                return t.get_new_title()
        self.log.error("Unknown sub window type.")

    def update_actived_window(self,window):
        if window is not None :
            self.log.debug("the window "+ window.windowTitle()+" is actived")
            winType = window.windowTitle().split("-")[0]
            gl.set_value(winType, window)
        else:
            self.log.debug("All the sub windows are inactived")

    def update_closed_window(self,info):
        self.log.info("the window "+ info+" is closed")
        winType = info.split("-")[0]
        self.log.info(winType)
        gl.set_value(winType, None)
        gl.delete_value(info)


class MySubQMdiSubWindow(QtWidgets.QMdiSubWindow):
    signal_close = QtCore.pyqtSignal(str)
    def __init__(self):
        super(QtWidgets.QMdiSubWindow, self).__init__()

    def closeEvent(self, event):
        self.signal_close.emit(self.windowTitle())