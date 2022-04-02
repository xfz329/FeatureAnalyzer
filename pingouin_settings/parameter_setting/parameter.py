#   -*- coding:utf-8 -*-
#   The parameter.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:10 on 2022/4/2

from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel

import pingouin as pg
from data import Globalvar as gl
from pingouin_settings.parameter_setting.parameter_basic import Ui_MainWindow
from process.task import Task
from utils.logger import Logger


class Ui_Parameter_MainWindow(Ui_MainWindow):
    def __init__(self, win_manager):
        super(Ui_Parameter_MainWindow, self).__init__()
        self.setupUi(self)
        self.log = Logger('fa').get_log()
        self.win_manager = win_manager

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

        self.add_to_1 = True
        self.add_to_2 = True
        self.add_to_3 = True
        self.add_to_4 = True

        self.pushButton_1.clicked.connect(self.clicked_button_1)
        self.pushButton_2.clicked.connect(self.clicked_button_2)
        self.pushButton_3.clicked.connect(self.clicked_button_3)
        self.pushButton_4.clicked.connect(self.clicked_button_4)
        self.pushButton_start.clicked.connect(self.start_analyse)
        self.pushButton_help.clicked.connect(self.show_help)

        self.task = Task(self.info_analyse_finished, "statistic")

    def start_analyse(self):
        self.log.info("empty method!")
        df = pg.read_dataset('anova')
        # para = {'dv':'Pain threshold', 'between':'Hair color', 'data':df,'detailed':True}
        self.task.set_worker(pg.anova, dv='Pain threshold', between='Hair color', data=df, detailed=True)
        raise NotImplementedError

    def show_help(self):
        self.log.info("empty method!")
        raise NotImplementedError

    def info_analyse_finished(self):
        self.log.info("get the answer calculated in the thread")
        win = self.win_manager.get_sub_window("Window_Result")
        self.log.info(self.task.get_ans())
        win.setText(str(self.task.get_ans()))
        self.log.info("empty method!")
        raise NotImplementedError

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
        temp = pg.list_dataset().index.tolist()
        for t in temp:
            self.comboBox_database.addItem(t)

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
        self.listView_all.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_all.clicked.connect(self.enable_all_buttons)

        self.listView_1.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_1.clicked.connect(self.disable_button_1)

        self.listView_2.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_2.clicked.connect(self.disable_button_2)

        self.listView_3.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_3.clicked.connect(self.disable_button_3)

        self.listView_4.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_4.clicked.connect(self.disable_button_4)

    def enable_all_buttons(self):
        self.add_to_1 = True
        self.add_to_2 = True
        self.add_to_3 = True
        self.add_to_4 = True
        self.pushButton_1.setText("添加")
        self.pushButton_2.setText("添加")
        self.pushButton_3.setText("添加")
        self.pushButton_4.setText("添加")

    def disable_button_1(self):
        self.add_to_1 = False
        self.pushButton_1.setText("移除")

    def disable_button_2(self):
        self.add_to_2 = False
        self.pushButton_2.setText("移除")

    def disable_button_3(self):
        self.add_to_3 = False
        self.pushButton_3.setText("移除")

    def disable_button_4(self):
        self.add_to_4 = False
        self.pushButton_4.setText("移除")

    # def change_button_1(self):
    #
    # def change_button_2(self):
    #
    # def change_button_3(self):
    #
    # def change_button_4(self):

    def exchange_selected_list(self, start, end):
        selected = start.selectedIndexes()
        for i in selected:
            num = i.row()
            temp = start.model().stringList()
            line = temp[num]
            del (temp[num])
            start.model().setStringList(temp)
            temp = end.model().stringList()
            temp.append(line)
            end.model().setStringList(temp)

    def clicked_button_1(self):
        if self.add_to_1:
            self.exchange_selected_list(self.listView_all,self.listView_1)
        else:
            self.exchange_selected_list(self.listView_1,self.listView_all)

    def clicked_button_2(self):
        if self.add_to_2:
            self.exchange_selected_list(self.listView_all,self.listView_2)
        else:
            self.exchange_selected_list(self.listView_2,self.listView_all)

    def clicked_button_3(self):
        if self.add_to_3:
            self.exchange_selected_list(self.listView_all,self.listView_3)
        else:
            self.exchange_selected_list(self.listView_3,self.listView_all)

    def clicked_button_4(self):
        if self.add_to_4:
            self.exchange_selected_list(self.listView_all,self.listView_4)
        else:
            self.exchange_selected_list(self.listView_4,self.listView_all)

    def set_method_name(self,s):
        self.label_method.setText(s)





