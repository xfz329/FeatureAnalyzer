#   -*- coding:utf-8 -*-
#   The setparameter.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:10 on 2022/4/2

import pingouin as pg
from PyQt5.QtCore import QStringListModel
from statistics_tools.pingouin.setparameter.parameter_basic2 import Ui_MainWindow

from utils.logger import Logger
from data import Globalvar as gl


class Ui_Parameter_MainWindow(Ui_MainWindow):
    def __init__(self, win_manager):
        super(Ui_Parameter_MainWindow, self).__init__()
        self.setupUi(self)
        self.log = Logger('fa').get_log()
        self.win_manager = win_manager
        self.pushButton_help.clicked.connect(self.show_help)

        self.prepare_data()

        self.list_model_all = QStringListModel()
        self.listView_all.setModel(self.list_model_all)

        self.list_model_1 = QStringListModel()
        self.listView_1.setModel(self.list_model_1)

        self.list_model_2 = QStringListModel()
        self.listView_2.setModel(self.list_model_2)

        self.list_model_3 = QStringListModel()
        self.listView_3.setModel(self.list_model_3)

        self.list_model_4 = QStringListModel()
        self.listView_4.setModel(self.list_model_4)


        self.init_list_view()



        self.show_set_parameters(2)
        self.show_choose_parameters(2)
        self.show_add_parameter(2)


    def show_help(self):
        pass


    def show_set_parameters(self, num):
        discard = 4 - num
        if discard < 0 or discard >4:
            self.log.error("num is too large to set parameters")
            return
        if discard > 0 :
            self.lineEdit_s4.setVisible(False)
            self.label_s4.setVisible(False)
            discard = discard -1
        else:
            return
        if discard > 0 :
            self.lineEdit_s3.setVisible(False)
            self.label_s3.setVisible(False)
            discard = discard -1
        else:
            return
        if discard > 0 :
            self.lineEdit_s2.setVisible(False)
            self.label_s2.setVisible(False)
            discard = discard -1
        else:
            return
        if discard > 0 :
            self.lineEdit_s1.setVisible(False)
            self.label_s1.setVisible(False)
            return

    def show_choose_parameters(self,num):
        discard = 4 - num
        if discard < 0 or discard >4:
            self.log.error("num is too large to set parameters")
            return
        if discard > 0 :
            self.comboBox_p4.setVisible(False)
            self.label_p4.setVisible(False)
            discard = discard -1
        else:
            return
        if discard > 0 :
            self.comboBox_p3.setVisible(False)
            self.label_p3.setVisible(False)
            discard = discard -1
        else:
            return
        if discard > 0 :
            self.comboBox_p2.setVisible(False)
            self.label_p2.setVisible(False)
            discard = discard -1
        else:
            return
        if discard > 0 :
            self.comboBox_p1.setVisible(False)
            self.label_p1.setVisible(False)
            return

    def show_add_parameter(self,num):
        discard = 4 - num
        if discard < 0 or discard > 4:
            self.log.error("num is too large to choose parameters")
            return
        if discard > 0:
            self.pushButton_4.setVisible(False)
            self.listView_4.setVisible(False)
            self.label_l4.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.pushButton_3.setVisible(False)
            self.listView_3.setVisible(False)
            self.label_l3.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.pushButton_2.setVisible(False)
            self.listView_2.setVisible(False)
            self.label_l2.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.pushButton_1.setVisible(False)
            self.listView_1.setVisible(False)
            self.label_l1.setVisible(False)
            return

    def prepare_data(self):
        self.comboBox_window.addItem("")
        for key in gl.get_dict():
            if key.startswith(gl.get_value("Window_Data")+'-'):
                win = gl.get_value(key)
                if win.isDataBounded(False):
                    self.comboBox_window.addItem(key)

        self.comboBox_database.addItem("")
        list = pg.list_dataset().index.tolist()
        for l in list:
            self.comboBox_database.addItem(l)

        self.comboBox_window.activated.connect(self.load_data_from_win)
        self.comboBox_database.activated.connect(self.load_data_from_database)

    def load_data_from_win(self):
        win_name = self.comboBox_window.currentText()
        if win_name != "":
            win = gl.get_value(win_name)
            columns = win.model().dataFrameColumns()
            self.list_model_all.setStringList(columns)

    def load_data_from_database(self):
        database = self.comboBox_database.currentText()
        if database != "":
            df = pg.read_dataset(database)
            columns = df.columns
            win = self.win_manager.get_sub_window("Window_Data")
            if df is not None:
                widget = win.widget()
                widget.model().setDataFrame(df)
            self.list_model_all.setStringList(columns)


    def init_list_view(self):
        pass
