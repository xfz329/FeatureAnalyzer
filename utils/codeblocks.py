import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from father.dir import Ui_MainWindow_F


class Ui_MainWindow_S(Ui_MainWindow_F):
    def __init__(self):
        super(Ui_MainWindow_S, self).__init__()
        self.setupUi(self)

    def setupUi(self,MainWindow):
        pass