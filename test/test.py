from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import  *
from utils.logger import  Logger

class Test(object):
    def __init__(self):
        super(Test,self).__init__()
        self.r = Rabbit()
        self.t =Tortoise()
        self.r.sinOut.connect(self.rr)
        self.t.sinOut.connect(self.tt)
        self.log = Logger('fa').get_log()

    def start(self):
        self.log.info("start")
        self.r.start()
        self.t.start()

    def rr(self,str):
        self.log.info(str)

    def tt(self,str):
        self.log.info(str)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 267)
        MainWindow.setWindowTitle("龟兔赛跑") # 设置窗口标题
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建兔子比赛标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 91, 21))
        self.label.setObjectName("label")
        self.label.setText("兔子的比赛记录")
        # 显示兔子的比赛记录
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 161, 191))
        self.textEdit.setObjectName("textEdit")
        # 创建乌龟比赛标签
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("乌龟的比赛记录")
        # 显示乌龟的比赛记录
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 40, 161, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        # 创建“开始比赛”按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("开始比赛")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.r=Rabbit() # 创建兔子线程对象
        self.r.sinOut.connect(self.rabbit) # 将线程信号连接到槽函数
        self.t = Tortoise() # 创建乌龟线程对象
        self.t.sinOut.connect(self.tortoise) # 将线程信号连接到槽函数
        self.pushButton.clicked.connect(self.start) # 开始两个线程

        self.log = Logger('fa').get_log()

    def start(self):
        self.log.info("start")
        self.r.start() # 启动兔子线程
        self.t.start() # 启动乌龟线程

    # 显示兔子的跑步距离
    def rabbit(self,str):
        self.textEdit.setPlainText(self.textEdit.toPlainText() + str+'\n')
        self.log.info(str)

    # 显示乌龟的跑步距离
    def tortoise(self, str):
        self.textEdit_2.setPlainText(self.textEdit_2.toPlainText() + str+'\n')
        self.log.info(str)

class Rabbit(QThread):
    sinOut = QtCore.pyqtSignal(str)
    def __init__(self):
        super(Rabbit,self).__init__()
        self.log = Logger('fa').get_log()
    def run(self):
        for i in range(1,11):
            QThread.msleep(100)
            self.sinOut.emit("Rabbit has run for "+str(i)+"00 meters.")
            self.log.info("inside the rabbit")
            if i == 9:
                self.sinOut.emit("Rabbit is sleeping.")
                QThread.sleep(5)
            if i == 10:
                self.sinOut.emit("Rabbit comes to the ending.")

class Tortoise(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super(Tortoise,self).__init__()
        self.log = Logger('fa').get_log()
    def run(self):
        for i in range(1,11):
            QThread.msleep(500)
            self.log.info("inside the tortoise")
            self.sinOut.emit("Tortoise has run for "+str(i)+"00 meters.")
            if i == 10:
                self.sinOut.emit("Tortoise comes to the ending.")

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    num = 3

    if num == 0 :
        # 多线程失败
        test = Test()
        test.start()
    elif num == 1:
        # 没有GUI ，多线程成功
        app= QApplication(sys.argv)
        test = Test()
        test.start()
        sys.exit(app.exec_())
        ## 没有gui界面，需要人工停止
    else:
        # 具有GUI ，多线程成功
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
        ui = Ui_MainWindow()  # 创建PyQt5设计的窗体对象
        ui.setupUi(MainWindow)  # 调用PyQt5窗体的方法对窗体对象进行初始化设置
        MainWindow.show()  # 显示窗体
        sys.exit(app.exec_())  # 程序关闭时退出进程