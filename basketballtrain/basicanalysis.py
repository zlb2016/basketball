# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basicanalysis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1246, 859)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dribble = QtWidgets.QToolButton(self.centralwidget)
        self.dribble.setGeometry(QtCore.QRect(200, 50, 131, 41))
        self.dribble.setObjectName("dribble")
        self.passball = QtWidgets.QToolButton(self.centralwidget)
        self.passball.setGeometry(QtCore.QRect(510, 50, 131, 41))
        self.passball.setObjectName("passball")
        self.threestep = QtWidgets.QToolButton(self.centralwidget)
        self.threestep.setGeometry(QtCore.QRect(830, 50, 131, 41))
        self.threestep.setObjectName("threestep")
        self.videolabel = QtWidgets.QLabel(self.centralwidget)
        self.videolabel.setGeometry(QtCore.QRect(90, 190, 651, 451))
        self.videolabel.setObjectName("videolabel")
        self.open = QtWidgets.QToolButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(160, 690, 111, 31))
        self.open.setObjectName("open")
        self.analysistextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.analysistextEdit.setGeometry(QtCore.QRect(780, 230, 441, 411))
        self.analysistextEdit.setObjectName("analysistextEdit")
        self.analabel = QtWidgets.QLabel(self.centralwidget)
        self.analabel.setGeometry(QtCore.QRect(800, 175, 41, 41))
        self.analabel.setObjectName("analabel")
        self.analysis = QtWidgets.QToolButton(self.centralwidget)
        self.analysis.setGeometry(QtCore.QRect(340, 690, 111, 31))
        self.analysis.setObjectName("analysis")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dribble.clicked.connect(MainWindow.close)
        self.passball.clicked.connect(MainWindow.close)
        self.threestep.clicked.connect(MainWindow.close)
        #self.open.clicked.connect(MainWindow.close)
        self.analysis.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基础动作分析"))
        self.dribble.setText(_translate("MainWindow", "运球"))
        self.passball.setText(_translate("MainWindow", "传球"))
        self.threestep.setText(_translate("MainWindow", "三步上篮"))
        self.videolabel.setText(_translate("MainWindow", "视频文件"))
        self.open.setText(_translate("MainWindow", "打开视频"))
        self.analabel.setText(_translate("MainWindow", "分析："))
        self.analysis.setText(_translate("MainWindow", "分析"))

