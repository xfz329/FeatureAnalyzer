#   -*- coding:utf-8 -*-
#   The subwindow_manager.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 10:07 on 2022/3/29
import data.Globalvar as gl
from utils.logger import Logger
from ui.subwindow.subwindow_data import SubWindow_Data
from ui.subwindow.subwindow_plot import SubWindow_Plot
from ui.subwindow.subwindow_logs import SubWindow_Logs
from ui.subwindow.subwindow_result import SubWindow_Result

class SubwindowManager(object):

    def __init__(self,area):
        gl.set_value("Window_Data","数据窗口")
        gl.set_value("Window_Plot", "绘图窗口")
        gl.set_value("Window_Logs", "日志窗口")
        gl.set_value("Window_Result", "输出窗口")
        self.mdi_area = area
        self.log = Logger("fa").get_log()
        self.mdi_area.subWindowActivated.connect(self.update_actived_window)

    def add_sub_window(self,Type):
        sub = Type()
        self.save_sub_window(sub)
        self.mdi_area.addSubWindow(sub)  # 将新建的子窗口添加到MDI区域
        sub.show()

    def save_sub_window(self,sub_win):
        gl.set_value(sub_win.windowTitle() , sub_win)
        gl.set_value(sub_win.win_type, sub_win)

    def get_sub_window(self,win_type):
        win = gl.get_value(win_type)
        if gl.get_value(win) is None:
            self.log.warning("There's none of "+win+" exits. Creating a new one.")
            if win_type == "Window_Data":
                self.add_sub_window(SubWindow_Data)
            elif win_type == "Window_Plot":
                self.add_sub_window(SubWindow_Plot)
            elif win_type == "Window_Logs":
                self.add_sub_window(SubWindow_Logs)
            elif win_type == "Window_Result":
                self.add_sub_window(SubWindow_Result)
            else:
                self.log.error("Get a request to create a unknown type("+win+") sub window")
                return
        return gl.get_value(win)

    def update_actived_window(self,window):
        aw = self.mdi_area.activeSubWindow()
        if aw is not None :
            self.log.debug("the window "+ aw.windowTitle()+" is actived")
            winType = aw.windowTitle().split("-")[0]
            gl.set_value(winType, aw)
        else:
            self.log.debug("None sub window is inactived")
