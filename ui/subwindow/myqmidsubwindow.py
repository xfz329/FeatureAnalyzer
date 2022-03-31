#   -*- coding:utf-8 -*-
#   The myqmidsubwindow.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 16:55 on 2022/3/31
from PyQt5 import QtCore, QtWidgets
from utils.logger import Logger
from data import Globalvar as gl


class MyQMdiSubWindow(QtWidgets.QMdiSubWindow):
    signal_close = QtCore.pyqtSignal(str)
    default_width = 800
    default_height = 600

    def __init__(self):
        super(QtWidgets.QMdiSubWindow, self).__init__()
        self.log = Logger('fa').get_log()
        self.win_type = None
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.resize(MyQMdiSubWindow.default_width, MyQMdiSubWindow.default_height)
        self.signal_close.connect(self.update_closed_window)

    def generate_title(self, num):
        return self.win_type + "-" + str(num)

    def closeEvent(self, event):
        self.log.info("about to close "+self.windowTitle())
        self.signal_close.emit(self.windowTitle())

    def update_closed_window(self,info):
        self.log.info("the window "+ info+" is closed")
        win = gl.get_value(info,None)
        if win is not None:
            # 使被点击关闭的窗口不再获得焦点
            win.setEnabled(False)
            # self.log.info(self.mdi_area.subWindowList())
        winType = info.split("-")[0]
        self.log.info(winType)
        gl.set_value(winType, None)
        gl.delete_value(info)