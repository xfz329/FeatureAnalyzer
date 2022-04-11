#   -*- coding:utf-8 -*-
#   The subwindow_pingouin.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 17:22 on 2022/4/10
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import QStringListModel

import pingouin as pg
from process.task import Task
from ui.subwindow.subwindow_pingouin_basic import SubWindow_Pingouin_basic
from data import Globalvar as gl

class SubWindow_Pingouin(SubWindow_Pingouin_basic):
    def __init__(self):
        SubWindow_Pingouin_basic.__init__(self)
        SubWindow_Pingouin_basic.adjustCount(self)

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

        self.list_model_5 = QStringListModel()
        self.listView_5.setModel(self.list_model_5)

        self.init_list_view()

        self.add_to_1 = True
        self.add_to_2 = True
        self.add_to_3 = True
        self.add_to_4 = True
        self.add_to_5 = True

        self.pushButton_1.clicked.connect(self.clicked_button_1)
        self.pushButton_2.clicked.connect(self.clicked_button_2)
        self.pushButton_3.clicked.connect(self.clicked_button_3)
        self.pushButton_4.clicked.connect(self.clicked_button_4)
        self.pushButton_5.clicked.connect(self.clicked_button_5)
        self.pushButton_start.clicked.connect(self.start_analyse)
        self.pushButton_help.clicked.connect(self.show_help)

        self.task = Task(self.info_analyse_finished, "statistic")

        self.df = None
        self.paras = {}
        self.desc = {}

        self.url = None
        self.columns = {}
        self.set_columns()

    def set_widgets(self):
        raise NotImplementedError

    def start_analyse(self):
        raise NotImplementedError

    def show_help(self):
        from PyQt5.QtCore import QUrl
        from PyQt5.QtGui import QDesktopServices
        QDesktopServices.openUrl(QUrl(self.url))

    def info_analyse_finished(self):
        self.desc["finish_time"] = QtCore.QDateTime.currentDateTime().toString("HH:mm:ss.zzz")
        ans = self.task.get_ans()
        self.log.info("get the answer calculated in the thread")
        self.log.info(ans)
        import pandas
        if type(ans) == pandas.core.frame.DataFrame:
            ans.rename(columns=self.columns, inplace=True)
        win = gl.get_value("Win_manager").get_sub_window("Window_Result")
        output = gl.get_value("output")
        output.add(self.desc,self.paras,ans)
        win.setText(output.get())
        self.log.info("finished updating")

    def info_draw_finished(self):
        self.desc["finish_time"] = QtCore.QDateTime.currentDateTime().toString("HH:mm:ss.zzz")
        win = gl.get_value("Win_manager").get_sub_window("Window_Result")
        output = gl.get_value("output")
        output.add(self.desc,self.paras)
        win.setText(output.get())
        self.log.info("finished drawing")

    def show_set_parameters(self, num):
        discard = 8 - num
        if discard < 0 or discard > 8:
            self.log.error("num is too large to set parameters")
            return
        if discard > 0:
            self.lineEdit_s8.setVisible(False)
            self.label_s8.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s7.setVisible(False)
            self.label_s7.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s6.setVisible(False)
            self.label_s6.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s5.setVisible(False)
            self.label_s5.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s4.setVisible(False)
            self.label_s4.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s3.setVisible(False)
            self.label_s3.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s2.setVisible(False)
            self.label_s2.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.lineEdit_s1.setVisible(False)
            self.label_s1.setVisible(False)
            return

    def show_choose_parameters(self, num):
        discard = 8 - num
        if discard < 0 or discard > 8:
            self.log.error("num is too large to set parameters")
            return
        if discard > 0:
            self.comboBox_p8.setVisible(False)
            self.label_p8.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p7.setVisible(False)
            self.label_p7.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p6.setVisible(False)
            self.label_p6.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p5.setVisible(False)
            self.label_p5.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p4.setVisible(False)
            self.label_p4.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p3.setVisible(False)
            self.label_p3.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p2.setVisible(False)
            self.label_p2.setVisible(False)
            discard = discard - 1
        else:
            return
        if discard > 0:
            self.comboBox_p1.setVisible(False)
            self.label_p1.setVisible(False)
            return

    def show_add_parameter(self, num):
        discard = 5 - num
        if discard < 0 or discard > 5:
            self.log.error("num is too large to choose parameters")
            return
        if discard > 0:
            self.pushButton_5.setVisible(False)
            self.listView_5.setVisible(False)
            self.label_l5.setVisible(False)
            discard = discard - 1
        else:
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
            if key.startswith(gl.get_value("Window_Data") + '-'):
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
            self.df = win.model().dataFrame()

    def load_data_from_database(self):
        database = self.comboBox_database.currentText()
        if database != "":
            df = pg.read_dataset(database)
            columns = df.columns
            win = gl.get_value("Win_manager").get_sub_window("Window_Data")
            self.df = df
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

        self.listView_5.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_5.clicked.connect(self.disable_button_5)

    def enable_all_buttons(self):
        self.add_to_1 = True
        self.add_to_2 = True
        self.add_to_3 = True
        self.add_to_4 = True
        self.add_to_5 = True
        self.pushButton_1.setText("添加")
        self.pushButton_2.setText("添加")
        self.pushButton_3.setText("添加")
        self.pushButton_4.setText("添加")
        self.pushButton_5.setText("添加")

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

    def disable_button_5(self):
        self.add_to_5 = False
        self.pushButton_5.setText("移除")

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
            self.exchange_selected_list(self.listView_all, self.listView_1)
        else:
            self.exchange_selected_list(self.listView_1, self.listView_all)

    def clicked_button_2(self):
        if self.add_to_2:
            self.exchange_selected_list(self.listView_all, self.listView_2)
        else:
            self.exchange_selected_list(self.listView_2, self.listView_all)

    def clicked_button_3(self):
        if self.add_to_3:
            self.exchange_selected_list(self.listView_all, self.listView_3)
        else:
            self.exchange_selected_list(self.listView_3, self.listView_all)

    def clicked_button_4(self):
        if self.add_to_4:
            self.exchange_selected_list(self.listView_all, self.listView_4)
        else:
            self.exchange_selected_list(self.listView_4, self.listView_all)

    def clicked_button_5(self):
        if self.add_to_5:
            self.exchange_selected_list(self.listView_all, self.listView_5)
        else:
            self.exchange_selected_list(self.listView_5, self.listView_all)

    def set_columns(self):
        self.columns.setdefault("Source", "变量名(Source)")
        self.columns.setdefault("SS", "平方和(Sums of squares)")
        self.columns.setdefault("DF", "自由度(Degrees of freedom)")
        self.columns.setdefault("ddof1", "自由度分子")
        self.columns.setdefault("ddof2", "自由度分母")
        self.columns.setdefault("MS", "均方(Mean square)")
        self.columns.setdefault("F", "F值")
        self.columns.setdefault("p-unc", "未校验的p值(uncorrected p-values)")
        self.columns.setdefault("n2", "η2")
        self.columns.setdefault("np2", "偏η2")
        self.columns.setdefault("ng2", "generalized eta squared")
        # 'eps': Greenhouse-Geisser epsilon factor (= index of sphericity)
        #
        # 'p-GG-corr': Greenhouse-Geisser corrected p-value
        #
        # 'W-spher': Sphericity test statistic
        #
        # 'p-spher': p-value of the sphericity test
        #
        # 'sphericity': sphericity of the data (boolean)
