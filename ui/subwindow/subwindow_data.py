#   -*- coding:utf-8 -*-
#   The subwindow_data.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:44 on 2022/3/31

from PyQt5.QtWidgets import QMessageBox
from ui.subwindow.myqmidsubwindow import MyQMdiSubWindow
from data import Globalvar as gl

class SubWindow_Data(MyQMdiSubWindow):
    count = 0
    def __init__(self):
        MyQMdiSubWindow.__init__(self)
        self.win_type = gl.get_value("Window_Data")
        SubWindow_Data.count += 1
        self.setWindowTitle(self.generate_title(SubWindow_Data.count))

        from qtpandas.views.DataTableView import DataTableWidget
        from qtpandas.models.DataFrameModel import DataFrameModel

        widget = DataTableWidget()
        widget.tableView.setSortingEnabled(False)
        model = DataFrameModel()
        widget.setViewModel(model)

        self.setWidget(widget)

    def isDataBounded(self,showDialog=False):
        if self.widget().model().dataFrame().empty:
            if showDialog:
                QMessageBox.warning(None, '警告', '当前数据窗口(' + self.windowTitle() + ')无数据可供绘制', QMessageBox.Ok)
            return False
        return True

    def isDataSelected(self,showDialog=False):
        index = self.widget().tableView.selectedIndexes()
        if len(index) == 0:
            if showDialog:
                QMessageBox.warning(None, '警告', '当前数据窗口(' + self.windowTitle() + ')没有任何数据被选中！', QMessageBox.Ok)
            return False
        return True

    def isPreparedToDraw(self):
        state = self.isDataBounded(True) and self.isDataSelected(True)
        if state:
           self.log.info("当前数据窗口 " + self.windowTitle()+ " 准备就绪，可以用于作图 ")
        else:
            self.log.warning("当前数据窗口 " + self.windowTitle()+ " 无绑定数据或无数据处于被选中状态，不可用于作图 ")
        return state

    def model(self):
        return self.widget().model()