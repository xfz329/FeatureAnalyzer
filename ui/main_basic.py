# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_new_win = QtWidgets.QMenu(self.menu_3)
        self.menu_new_win.setObjectName("menu_new_win")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menu_5)
        self.menu_6.setObjectName("menu_6")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_author = QtWidgets.QAction(MainWindow)
        self.action_author.setObjectName("action_author")
        self.action_logs = QtWidgets.QAction(MainWindow)
        self.action_logs.setObjectName("action_logs")
        self.action_tileSubWin = QtWidgets.QAction(MainWindow)
        self.action_tileSubWin.setObjectName("action_tileSubWin")
        self.action_cascadeSubWin = QtWidgets.QAction(MainWindow)
        self.action_cascadeSubWin.setObjectName("action_cascadeSubWin")
        self.action_draw = QtWidgets.QAction(MainWindow)
        self.action_draw.setObjectName("action_draw")
        self.action_win_data = QtWidgets.QAction(MainWindow)
        self.action_win_data.setObjectName("action_win_data")
        self.action_win_plot = QtWidgets.QAction(MainWindow)
        self.action_win_plot.setObjectName("action_win_plot")
        self.action_win_log = QtWidgets.QAction(MainWindow)
        self.action_win_log.setObjectName("action_win_log")
        self.action_win_result = QtWidgets.QAction(MainWindow)
        self.action_win_result.setObjectName("action_win_result")
        self.action_kerner_scipy_stats = QtWidgets.QAction(MainWindow)
        self.action_kerner_scipy_stats.setCheckable(True)
        self.action_kerner_scipy_stats.setObjectName("action_kerner_scipy_stats")
        self.action_kerner_statsmodels = QtWidgets.QAction(MainWindow)
        self.action_kerner_statsmodels.setCheckable(True)
        self.action_kerner_statsmodels.setObjectName("action_kerner_statsmodels")
        self.action_kerner_pingouin = QtWidgets.QAction(MainWindow)
        self.action_kerner_pingouin.setCheckable(True)
        self.action_kerner_pingouin.setObjectName("action_kerner_pingouin")
        self.menu.addAction(self.action_open)
        self.menu_2.addAction(self.action_draw)
        self.menu_new_win.addAction(self.action_win_data)
        self.menu_new_win.addAction(self.action_win_plot)
        self.menu_new_win.addAction(self.action_win_log)
        self.menu_new_win.addAction(self.action_win_result)
        self.menu_3.addAction(self.menu_new_win.menuAction())
        self.menu_3.addAction(self.action_tileSubWin)
        self.menu_3.addAction(self.action_cascadeSubWin)
        self.menu_4.addAction(self.action_author)
        self.menu_4.addAction(self.action_logs)
        self.menu_6.addAction(self.action_kerner_scipy_stats)
        self.menu_6.addAction(self.action_kerner_statsmodels)
        self.menu_6.addAction(self.action_kerner_pingouin)
        self.menu_5.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "绘图"))
        self.menu_3.setTitle(_translate("MainWindow", "窗口"))
        self.menu_new_win.setTitle(_translate("MainWindow", "新建"))
        self.menu_4.setTitle(_translate("MainWindow", "关于"))
        self.menu_5.setTitle(_translate("MainWindow", "数据分析"))
        self.menu_6.setTitle(_translate("MainWindow", "分析内核选择"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_author.setText(_translate("MainWindow", "作者"))
        self.action_author.setShortcut(_translate("MainWindow", "F1"))
        self.action_logs.setText(_translate("MainWindow", "更新日志"))
        self.action_logs.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_tileSubWin.setText(_translate("MainWindow", "平铺显示"))
        self.action_cascadeSubWin.setText(_translate("MainWindow", "级联显示"))
        self.action_draw.setText(_translate("MainWindow", "绘制"))
        self.action_draw.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_win_data.setText(_translate("MainWindow", "数据窗口"))
        self.action_win_data.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.action_win_plot.setText(_translate("MainWindow", "绘图窗口"))
        self.action_win_plot.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.action_win_log.setText(_translate("MainWindow", "日志窗口"))
        self.action_win_log.setShortcut(_translate("MainWindow", "Ctrl+3"))
        self.action_win_result.setText(_translate("MainWindow", "输出窗口"))
        self.action_win_result.setShortcut(_translate("MainWindow", "Ctrl+4"))
        self.action_kerner_scipy_stats.setText(_translate("MainWindow", "Scipy.stats"))
        self.action_kerner_statsmodels.setText(_translate("MainWindow", "Statsmodels"))
        self.action_kerner_pingouin.setText(_translate("MainWindow", "Pingouin"))
from resource import label_rc
