#   -*- coding:utf-8 -*-
#   The main.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:40 on 2022/3/26

import pandas as pd
from PyQt5 import QtCore, QtWidgets

import data.Globalvar as gl
from ui.main_basic import Ui_MainWindow
from ui.subwindow.SubWindow import SubwindowManager
from utils.logger import Logger


class Global_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Global_MainWindow, self).__init__()
        gl.init_()
        self.current_file = None
        self.count = 0
        self.log = Logger('fa').get_log()
        self.swm = None

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        # self.mdiArea.setActivationOrder(QMdiArea.WindowOrder.ActivationHistoryOrder)
        self.swm = SubwindowManager(self.mdiArea)
        self.action_author.triggered.connect(self.show_author)
        self.action_logs.triggered.connect(self.show_changelogs)
        self.action_open.triggered.connect(self.open)
        self.menu_new_win.triggered.connect(self.create_new_subwindow)
        self.action_cascadeSubWin.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.action_tileSubWin.triggered.connect(self.mdiArea.tileSubWindows)
        self.action_draw.triggered.connect(self.draw)
        self.create_new_subwindow(self.action_win_data)
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

    def create_new_subwindow(self, action):
        if action.objectName() == self.action_win_data.objectName():
            self.swm.add_sub_window_data()
            return
        if action.objectName() == self.action_win_plot.objectName():
            self.swm.add_sub_window_plot()
            return
        if action.objectName() == self.action_win_log.objectName():
            self.swm.add_sub_window_logs()
            return
        if action.objectName() == self.action_win_result.objectName():
            self.swm.add_sub_window_result()
            return

    def open(self):
        win = self.swm.get_sub_window(SubwindowManager.Key_Window_Data)
        self.log.info("add data to subwindow "+ win.windowTitle())
        from process.Open import OpenFiles as of
        df = of().open()
        if df is not None:
            widget = win.widget()
            widget.model().setDataFrame(df)

    def draw(self):
        winD = self.swm.get_sub_window(SubwindowManager.Key_Window_Data)
        winP = self.swm.get_sub_window(SubwindowManager.Key_Window_Plot)
        self.log.info("draw plot to subwindow " + winP.windowTitle()+ " using selected data in subwindow " + winD.windowTitle())

        from process.Draw import Draw
        Draw().draw(winD,winP)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Global_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
