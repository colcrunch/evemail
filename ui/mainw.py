# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folders = QtWidgets.QScrollArea(self.centralwidget)
        self.folders.setGeometry(QtCore.QRect(10, 50, 181, 401))
        self.folders.setWidgetResizable(True)
        self.folders.setObjectName("folders")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 177, 397))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.folders.setWidget(self.scrollAreaWidgetContents)
        self.mail = QtWidgets.QScrollArea(self.centralwidget)
        self.mail.setGeometry(QtCore.QRect(200, 10, 681, 201))
        self.mail.setWidgetResizable(True)
        self.mail.setObjectName("mail")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 677, 197))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.mail.setWidget(self.scrollAreaWidgetContents_2)
        self.message = QtWidgets.QScrollArea(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(200, 220, 681, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setWidgetResizable(True)
        self.message.setObjectName("message")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 677, 227))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.message.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 81, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 10, 101, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Compose"))
        self.pushButton_2.setText(_translate("MainWindow", "Mark All Read"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionSettings.setText(_translate("MainWindow", "&Settings"))

