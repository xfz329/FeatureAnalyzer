#   -*- coding:utf-8 -*-
#   The parameter.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 15:31 on 2022/3/31

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QStringListModel
from statistics_tools.pingouin.parameter_basic import  Ui_MainWindow
from data import Globalvar as gl


class Ui_Parameter_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Ui_Parameter_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.comboBox_Subwindow.addItem("")
        for key in gl.get_dict():
            if key.startswith(gl.get_value("Window_Data")+'-'):
                win = gl.get_value(key)
                if win.isDataBounded(False):
                    self.comboBox_Subwindow.addItem(key)
        self.comboBox_Subwindow.activated.connect(self.load_data)

        self.list_columns = []
        self.slm = QStringListModel()
        self.slm.setStringList(self.list_columns)
        self.listView_all.setModel(self.slm)

        self.list_columns_bt = []
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.list_columns_bt)
        self.listView_bt.setModel(self.slm2)

        self.list_columns_vb = []
        self.slm3 = QStringListModel()
        self.slm3.setStringList(self.list_columns_vb)
        self.listView.setModel(self.slm3)

        self.listView_all.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_all.clicked.connect(self.changeButton)

        self.listView_bt.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_bt.clicked.connect(self.changeButton2)

        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView.clicked.connect(self.changeButton3)

        self.addTobt = True
        self.addTovb = True
        # self.pushButton_bt.setText("添加!!!!!!!!!")
        self.pushButton_bt.clicked.connect(self.button_process)
        self.pushButton_vb.clicked.connect(self.button_process2)


    def load_data(self):
        from PyQt5.QtWidgets import QMessageBox
        win_name = self.comboBox_Subwindow.currentText()
        if  win_name != "":
            # QMessageBox.information(None, "载入数据","获取 "+self.comboBox_Subwindow.currentText()+ " 中的内容成功",QMessageBox.Ok)
            win = gl.get_value(win_name)
            list = win.model().dataFrameColumns()
            # print(list)
            self.list_columns = list
            self.slm.setStringList(self.list_columns)

    def changeButton(self):
        self.addTobt = True
        self.addTovb = True
        self.pushButton_bt.setText("添加")
        self.pushButton_vb.setText("添加")
        pass

    def changeButton2(self):
        self.addTobt = False
        self.pushButton_bt.setText("移除")

    def changeButton3(self):
        self.addTovb = False
        self.pushButton_vb.setText("移除")

    def button_process(self):
        if self.addTobt:
            selected = self.listView_all.selectedIndexes()
            for i in selected:
                num = i.row()
                line = self.list_columns[i.row()]
                del(self.list_columns[num])
                self.slm.setStringList(self.list_columns)
                self.list_columns_bt.append(line)
                self.slm2.setStringList(self.list_columns_bt)
        else:
            selected = self.listView_bt.selectedIndexes()
            for i in selected:
                num = i.row()
                line = self.list_columns_bt[i.row()]
                del (self.list_columns_bt[num])
                self.slm2.setStringList(self.list_columns_bt)

                self.list_columns.append(line)
                self.slm.setStringList(self.list_columns)


    def button_process2(self):
        if self.addTovb:
            selected = self.listView_all.selectedIndexes()
            for i in selected:
                num = i.row()
                line = self.list_columns[i.row()]
                del(self.list_columns[num])
                self.slm.setStringList(self.list_columns)
                self.list_columns_vb.append(line)
                self.slm3.setStringList(self.list_columns_vb)
        else:
            selected = self.listView.selectedIndexes()
            for i in selected:
                num = i.row()
                line = self.list_columns_vb[i.row()]
                del (self.list_columns_vb[num])
                self.slm3.setStringList(self.list_columns_vb)

                self.list_columns.append(line)
                self.slm.setStringList(self.list_columns)

