#   -*- coding:utf-8 -*-
#   The SubWindow.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:07 on 2022/3/29
from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QMdiArea,QMdiSubWindow,QWidget, QVBoxLayout,QHBoxLayout,QFormLayout
from QCustomPlot2 import *
import data.Globalvar as gl

class SubwindowManager:
    DataWindow          =    0x0001
    PlotWindow          =    0x0010
    LogsWindow          =    0x0100
    ResultWindow        =    0x1000

    default_width  =    800
    default_height =    600

    def __init__(self,area):
        self.count_data = 0
        self.count_plot = 0
        self.count_logs = 0
        self.count_result = 0
        self.mdi_area = area


    def add_data_sub_window(self):
        from qtpandas.views.DataTableView import DataTableWidget
        from qtpandas.models.DataFrameModel import DataFrameModel

        sub = QtWidgets.QMdiSubWindow()  # 创建子窗口对象
        title = self.generate_win_title(SubwindowManager.DataWindow)
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
        # sub.closed.connect(self.Test)
        sub.show()

    def add_plot_sub_window(self):

        sub = QtWidgets.QMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.PlotWindow)
        sub.setWindowTitle(title)
        sub.resize(SubwindowManager.default_width, SubwindowManager.default_height)
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        plot = QCustomPlot(widget)
        layout.addWidget(plot)
        # sub.setLayout(layout)
        sub.setWidget(widget)
        self.mdi_area.addSubWindow(sub)
        sub.show()
        pass

    def add_logs_sub_window(self):
        sub = QtWidgets.QMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.LogsWindow)
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
        sub.show()


    def add_result_sub_window(self):
        sub = QtWidgets.QMdiSubWindow()
        title = self.generate_win_title(SubwindowManager.ResultWindow)
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
        sub.show()

    def generate_win_title(self, type):
        if  type == SubwindowManager.DataWindow:
            self.count_data += 1
            return self.update_index(self.count_data,"数据窗口")
        if  type == SubwindowManager.PlotWindow:
            self.count_plot += 1
            return self.update_index(self.count_plot,"图形窗口")
        if  type == SubwindowManager.LogsWindow:
            self.count_logs += 1
            return self.update_index(self.count_logs,"日志窗口")
        if  type == SubwindowManager.ResultWindow:
            self.count_result += 1
            return self.update_index(self.count_result,"输出窗口")

    def update_index(self,value,prefix):
        return prefix +"-"+ str(value)



    def Test(self):
        print("the sub window has been closed.")
        pass