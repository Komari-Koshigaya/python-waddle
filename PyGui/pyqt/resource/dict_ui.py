# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_nav = QtWidgets.QFrame(self.centralwidget)
        self.frame_nav.setEnabled(True)
        self.frame_nav.setGeometry(QtCore.QRect(0, 0, 151, 571))
        self.frame_nav.setMouseTracking(False)
        self.frame_nav.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_nav.setObjectName("frame_nav")
        self.pushButton = QtWidgets.QPushButton(self.frame_nav)
        self.pushButton.setGeometry(QtCore.QRect(30, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_left_2 = QtWidgets.QPushButton(self.frame_nav)
        self.pushButton_left_2.setGeometry(QtCore.QRect(30, 280, 93, 28))
        self.pushButton_left_2.setObjectName("pushButton_left_2")
        self.pushButton_left_3 = QtWidgets.QPushButton(self.frame_nav)
        self.pushButton_left_3.setGeometry(QtCore.QRect(30, 340, 93, 28))
        self.pushButton_left_3.setObjectName("pushButton_left_3")
        self.label_user = QtWidgets.QLabel(self.frame_nav)
        self.label_user.setGeometry(QtCore.QRect(20, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_user.setFont(font)
        self.label_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_user.setAutoFillBackground(False)
        self.label_user.setScaledContents(False)
        self.label_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user.setWordWrap(False)
        self.label_user.setOpenExternalLinks(False)
        self.label_user.setObjectName("label_user")
        self.frame_content = QtWidgets.QFrame(self.centralwidget)
        self.frame_content.setGeometry(QtCore.QRect(150, 0, 651, 571))
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_help = QtWidgets.QAction(MainWindow)
        self.action_help.setObjectName("action_help")
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_help)
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_left_3.clicked.connect(MainWindow.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主窗口"))
        self.pushButton.setText(_translate("MainWindow", "词典"))
        self.pushButton_left_2.setText(_translate("MainWindow", "翻译"))
        self.pushButton_left_3.setText(_translate("MainWindow", "生词本"))
        self.label_user.setText(_translate("MainWindow", "小小怪下士"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助(&F)"))
        self.action_about.setText(_translate("MainWindow", "关于"))
        self.action_about.setShortcut(_translate("MainWindow", "F4"))
        self.action_help.setText(_translate("MainWindow", "使用帮助"))
