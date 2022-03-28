#   -*- coding:utf-8 -*-
#   The main.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:40 on 2022/3/26

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui_main.main_basic import Ui_MainWindow
import data.Globalvar as gl
from utils.logger import Logger
import pandas as pd

class Global_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Global_MainWindow, self).__init__()
        gl.init_()
        self.current_file = None
        self.count = 0
        self.log = Logger('fa').get_log()

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.action_author.triggered.connect(self.show_author)
        self.action_logs.triggered.connect(self.show_changelogs)
        self.action_open.triggered.connect(self.open)
        self.action_new.triggered.connect(self.new)
        self.action_cascadeSubWin.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.action_tileSubWin.triggered.connect(self.mdiArea.tileSubWindows)
        self.action_draw.triggered.connect(self.draw)
        self.new()
        self.update_statusbar("系统初始化完毕")


    def show_author(self):
        from help.author import author
        self.about_author = author.Ui_Author_MainWindow()
        self.update_statusbar("显示作者信息")
        self.about_author.show()

    def show_changelogs(self):
        from help.changelogs import  changelogs
        self.about_changelogs = changelogs.Ui_Changelogs_MainWindow()
        self.update_statusbar("显示更新日志")
        self.about_changelogs.show()

    def update_statusbar(self,msg):
        self.statusbar.clearMessage()
        datetime = QtCore.QDateTime.currentDateTime()
        text = datetime.toString("HH:mm:ss")
        self.statusbar.showMessage(text+"  "+msg, 5000)

    def open(self):
        if gl.get_value("last_operation_widget")== None:
            self.log.warning("None widget exits. Add a new one.")
            self.new()
        widget = gl.get_value("last_operation_widget")
        self.log.info("last_operation_widget is "+ str(widget))
        from PyQt5.QtWidgets import QFileDialog
        f = QFileDialog.getOpenFileName(None,"打开","C:\\",".csv *.*")
        file = f[0]
        self.log.info("Open file"+file)
        self.update_statusbar("已选择文件"+file)
        if file.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.endswith(".xls") or file.endswith(".xlsx"):
            df = pd.read_excel(file)
        widget.model().setDataFrame(df)

    def new(self):
        from qtpandas.views.DataTableView import DataTableWidget
        from qtpandas.models.DataFrameModel import DataFrameModel
        sub = QMdiSubWindow()  # 创建子窗口对象
        self.count = self.count + 1  # 记录子窗口个数
        # 设置子窗口标题
        title = "数据窗口" + str(self.count)
        sub.setWindowTitle(title)
        # 在子窗口中添加一个标签，并设置文本
        widget = DataTableWidget()
        widget.tableView.setSortingEnabled(False)
        model = DataFrameModel()
        widget.setViewModel(model)
        sub.setWidget(widget)
        gl.set_value(title+"widget",widget)
        gl.set_value("last_operation_widget",widget)
        self.mdiArea.addSubWindow(sub)  # 将新建的子窗口添加到MDI区域
        if self.count == 1:
            sub.showMaximized()
        else:
            sub.show()  # 显示子窗口
        print(self.mdiArea.subWindowList())

    def draw(self):
        from PyQt5.QtWidgets import QMessageBox
        widget = gl.get_value("last_operation_widget")
        if widget is None:
            QMessageBox.warning(None, '警告', '没有任何数据窗口处于被打开的状态', QMessageBox.Ok)
            return
        if widget.model().dataFrame().empty:
            QMessageBox.warning(None, '警告', '当前数据窗口无数据可供绘制', QMessageBox.Ok)
            return
        index = widget.tableView.selectedIndexes()
        if len(index) == 0:
            QMessageBox.warning(None, '警告', '没有任何数据被选中！', QMessageBox.Ok)
            return
        for ix in index:
            print(ix.row(), ix.column())
        print(widget.tableView.selectedIndexes())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Global_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
