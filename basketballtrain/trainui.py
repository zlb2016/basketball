# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.basicaction = QtWidgets.QPushButton(self.centralwidget)
        self.basicaction.setGeometry(QtCore.QRect(30, 90, 121, 51))
        self.basicaction.setObjectName("basicaction")
        self.actiondetect = QtWidgets.QPushButton(self.centralwidget)
        self.actiondetect.setGeometry(QtCore.QRect(30, 200, 121, 51))
        self.actiondetect.setObjectName("actiondetect")
        self.foulanalysis = QtWidgets.QPushButton(self.centralwidget)
        self.foulanalysis.setGeometry(QtCore.QRect(30, 310, 121, 51))
        self.foulanalysis.setObjectName("foulanalysis")
        self.shootanalysis = QtWidgets.QPushButton(self.centralwidget)
        self.shootanalysis.setGeometry(QtCore.QRect(30, 420, 121, 51))
        self.shootanalysis.setObjectName("shootanalysis")
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(250, 40, 461, 501))
        self.label_pic.setText("")
        self.label_pic.setObjectName("label_pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.basicaction.clicked.connect(MainWindow.close)
        self.actiondetect.clicked.connect(MainWindow.close)
        self.foulanalysis.clicked.connect(MainWindow.close)
        self.shootanalysis.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "篮球运动员动作规范系统"))
        self.basicaction.setText(_translate("MainWindow", "基础动作分析"))
        self.actiondetect.setText(_translate("MainWindow", "篮球事件检测"))
        self.foulanalysis.setText(_translate("MainWindow", "犯规视频分析"))
        self.shootanalysis.setText(_translate("MainWindow", "投篮视频分析"))

