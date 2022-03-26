#   -*- coding:utf-8 -*-
#   The author.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:44 on 2022/3/26
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from help.author.author_basic import Ui_MainWindow
from utils import projectfiles


class Ui_Author_MainWindow(Ui_MainWindow):
    def __init__(self):
        super(Ui_Author_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.label.setText(self.getAuthor())

    def getAuthor(self):
        path = projectfiles.Files()
        with open(path.author, 'r', encoding="utf-8") as f:
            return f.read()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Author_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())