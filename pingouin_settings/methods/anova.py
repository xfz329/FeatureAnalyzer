#   -*- coding:utf-8 -*-
#   The anova.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:02 on 2022/4/2

from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel

import pingouin as pg
from data import Globalvar as gl
from pingouin_settings.parameter_setting.parameter import Ui_Parameter_MainWindow
from process.task import Task
from utils.logger import Logger


class Ui_Anova_MainWindow(Ui_Parameter_MainWindow):
    def __init__(self, win_manager):
        Ui_Parameter_MainWindow.__init__(self, win_manager)
        self.show_set_parameters(2)
        self.show_choose_parameters(2)
        self.show_add_parameter(2)
        self.set_method_name("ANOVA")


    def start_analyse(self):
        self.log.info("empty method!")
        df = pg.read_dataset('anova')
        # para = {'dv':'Pain threshold', 'between':'Hair color', 'data':df,'detailed':True}
        self.task.set_worker(pg.anova, dv='Pain threshold', between='Hair color', data=df, detailed=True)
        pass

    def show_help(self):
        self.log.info("empty method!")
        pass

    def info_analyse_finished(self):
        self.log.info("get the answer calculated in the thread")
        win = self.win_manager.get_sub_window("Window_Result")
        self.log.info(self.task.get_ans())
        win.setText(str(self.task.get_ans()))
        self.log.info("empty method!")
