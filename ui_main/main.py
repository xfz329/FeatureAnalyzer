#   -*- coding:utf-8 -*-
#   The main.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:40 on 2022/3/26

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui_main.main_basic import Ui_MainWindow


class Global_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Global_MainWindow, self).__init__()

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.action_author.triggered.connect(self.show_author)


    def show_author(self):
        from help.author import author
        self.about_author = author.Ui_Author_MainWindow()
        self.about_author.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Global_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
