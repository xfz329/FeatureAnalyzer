#   -*- coding:utf-8 -*-
#   The subwindow_result.py in FeatureAnalyzer
#   created by Jiang Feng(silencejiang@zju.edu.cn)
#   created at 19:15 on 2022/3/31

from PyQt5 import QtCore,QtWidgets
from ui.subwindow.myqmidsubwindow import MyQMdiSubWindow
from data import Globalvar as gl

class SubWindow_Result(MyQMdiSubWindow):
    count = 0
    def __init__(self):
        MyQMdiSubWindow.__init__(self)
        self.win_type = gl.get_value("Window_Result")
        SubWindow_Result.count += 1
        self.setWindowTitle(self.generate_title(SubWindow_Result.count))

        centralwidget = QtWidgets.QWidget()
        scrollArea = QtWidgets.QScrollArea(centralwidget)
        scrollArea.setWidgetResizable(True)
        scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, self.default_width - 20, self.default_height - 20))
        scrollArea.setWidget(scrollAreaWidgetContents)

        label = QtWidgets.QLabel(scrollAreaWidgetContents)
        label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)

        from help.author.author_template import Template
        label.setText(Template().get())

        formLayout = QtWidgets.QFormLayout(scrollAreaWidgetContents)
        formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)

        formLayout_2 = QtWidgets.QFormLayout(centralwidget)
        formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, scrollArea)

        self.setWidget(centralwidget)
        self.label = label

    def setText(self,s):
        temp = self.label.text()
        self.label.setText(temp+s)