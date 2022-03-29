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

    default_width  =    800
    default_height =    600

    def __init__(self,area):
        t_data = Title(SubwindowManager.Window_Data,"数据窗口")
        t_plot = Title(SubwindowManager.Window_Plot, "图形窗口")
        t_logs = Title(SubwindowManager.Window_Logs, "日志窗口")
        t_result = Title(SubwindowManager.Window_Result, "输出窗口")
        self.titles=[t_data,t_plot,t_logs,t_result]
        self.mdi_area = area
        self.log = Logger("fa").get_log()
        self.mdi_area.subWindowActivated.connect(self.update_actived_window)


    def add_data_sub_window(self):
        from qtpandas.views.DataTableView import DataTableWidget
        from qtpandas.models.DataFrameModel import DataFrameModel

        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Data)
        sub.setWindowTitle(title)
        sub.resize(SubwindowManager.default_width, SubwindowManager.default_height)
        # 在子窗口中添加一个标签，并设置文本
        widget = DataTableWidget()
        widget.tableView.setSortingEnabled(False)
        model = DataFrameModel()
        widget.setViewModel(model)
        sub.setWidget(widget)
        gl.set_value(title + "widget", widget)
        gl.set_value("last_operation_widget", widget)
        self.mdi_area.addSubWindow(sub)  # 将新建的子窗口添加到MDI区域
        sub.signal_close.connect(self.update_closed_window)
        sub.show()

    def add_plot_sub_window(self):

        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Plot)
        sub.setWindowTitle(title)
        sub.resize(SubwindowManager.default_width, SubwindowManager.default_height)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        plot = QCustomPlot(widget)
        layout.addWidget(plot)
        # sub.setLayout(layout)
        sub.setWidget(widget)
        self.mdi_area.addSubWindow(sub)
        sub.signal_close.connect(self.update_closed_window)
        sub.show()

    def add_logs_sub_window(self):
        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Logs)
        sub.setWindowTitle(title)
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
        self.mdi_area.addSubWindow(sub)
        sub.signal_close.connect(self.update_closed_window)
        sub.show()


    def add_result_sub_window(self):
        sub = MySubQMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.Window_Result)
        sub.setWindowTitle(title)
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
        self.mdi_area.addSubWindow(sub)
        sub.signal_close.connect(self.update_closed_window)
        sub.show()

    def generate_win_title(self, type):
        for t in self.titles:
            if t.is_winType(type):
                return t.get_new_title()
        self.log.error("Unknown sub window type.")

    def update_actived_window(self,window):
        if window is not None :
            self.log.debug("the window "+ window.windowTitle()+" is actived")
        else:
            self.log.debug("All the sub windows are inactived")

    def update_closed_window(self,info):
        self.log.info("the window "+ info+" is closed")


class MySubQMdiSubWindow(QtWidgets.QMdiSubWindow):
    signal_close = QtCore.pyqtSignal(str)
    def __init__(self):
        super(QtWidgets.QMdiSubWindow, self).__init__()

    def closeEvent(self, event):
        self.signal_close.emit(self.windowTitle())