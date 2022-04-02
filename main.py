#   -*- coding:utf-8 -*-
#   The main.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:40 on 2022/3/26

from PyQt5 import QtCore, QtWidgets

import data.Globalvar as gl
import pingouin_settings.methods as pm
from process.task_open import TaskOpen
from ui.main_basic import Ui_MainWindow
from ui.subwindow.subwindow_data import SubWindow_Data
from ui.subwindow.subwindow_logs import SubWindow_Logs
from ui.subwindow.subwindow_manager import SubwindowManager
from ui.subwindow.subwindow_plot import SubWindow_Plot
from ui.subwindow.subwindow_result import SubWindow_Result
from utils.logger import Logger


class Global_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Global_MainWindow, self).__init__()
        gl.init_()
        self.current_file = None
        self.log = Logger('fa').get_log()
        self.swm = None
        self.taskOpen = TaskOpen(self.updateWinData,"open")

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.menu_5.setToolTipsVisible(True)
        # self.mdiArea.setActivationOrder(QMdiArea.WindowOrder.ActivationHistoryOrder)
        self.swm = SubwindowManager(self.mdiArea)
        self.action_author.triggered.connect(self.show_author)
        self.action_logs.triggered.connect(self.show_changelogs)
        self.action_open.triggered.connect(self.open)
        self.menu_new_win.triggered.connect(self.create_new_subwindow)
        self.menu_kernel.triggered.connect(self.choose_kernel)
        self.action_cascadeSubWin.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.action_tileSubWin.triggered.connect(self.mdiArea.tileSubWindows)
        self.action_draw.triggered.connect(self.draw)
        self.create_new_subwindow(self.action_win_data)
        self.action_T.triggered.connect(self.set_para)
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

    def choose_kernel(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(None,"分析内核设置","目前所有统计分析功能均通过Pingouin（0.5.1）完成。Pingouin内部使用了部分SciPy.stats的统计分析功能。其他分析内核功能请期待版本更新。",QMessageBox.Ok)

    def create_new_subwindow(self, action):
        if action.objectName() == self.action_win_data.objectName():
            self.swm.add_sub_window(SubWindow_Data)
            return
        if action.objectName() == self.action_win_plot.objectName():
            self.swm.add_sub_window(SubWindow_Plot)
            return
        if action.objectName() == self.action_win_log.objectName():
            self.swm.add_sub_window(SubWindow_Logs)
            return
        if action.objectName() == self.action_win_result.objectName():
            self.swm.add_sub_window(SubWindow_Result)
            return

    def open(self):
        win = self.swm.get_sub_window("Window_Data")
        self.log.info("add data to subwindow "+ win.windowTitle())
        gl.set_value("WinToAddData",win)
        self.taskOpen.set_worker()

    def updateWinData(self):
        win = gl.get_value("WinToAddData")
        df = self.taskOpen.get_ans()
        if df is not None:
            widget = win.widget()
            widget.model().setDataFrame(df)

    def draw(self):
        winD = self.swm.get_sub_window("Window_Data")
        if not winD.isPreparedToDraw():
            return
        winP = self.swm.get_sub_window("Window_Plot")
        self.log.info("draw plot to subwindow " + winP.windowTitle()+ " using selected data in subwindow " + winD.windowTitle())

        from process.Draw import Draw
        Draw().draw(winD,winP)

    def set_para(self):
        self.para =pm.Ui_Anova_MainWindow(self.swm)
        self.para.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Global_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
