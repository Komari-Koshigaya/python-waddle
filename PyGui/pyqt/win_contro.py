#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author :        NIEJUN 
# Datetime：      2020/8/26 8:53
# IDE:            PyCharm
# File Name：     win_contro.py
# DESCRIP：   ui的控制逻辑
import sys
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from util.logger import console_logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from resource.login_ui import Ui_Dialog
from resource.dict_ui import Ui_MainWindow

# 打印日志信息
logger = console_logging(logging.DEBUG)


# 登录界面的控制逻辑
class Login(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('b.ico'))
        self.login_btn.setStyleSheet('''color: white; background-color: rgb(218,181,150);''')
        self.regi_btn.setStyleSheet('''color: white; background-color: rgb(218,181,150);''')
        # 实例化一个主窗口界面
        self.dict_win = DictWin()
        self.login_btn.clicked.connect(self.end_event)  # 绑定登陆函数

    # 登陆函数
    def end_event(self):
        if self.name_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入姓名')
        elif self.pwd_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入密码')
        else:
            QMessageBox.information(self, '登陆', self.name_edit.text() + ' 欢迎登陆')
            logger.debug("退出程序")
            self.dict_win.show()   # 显示主窗口
            self.close()  # 关闭登录窗口

    # 键盘按下esc键退出登录界面
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


# 主界面的控制逻辑
class DictWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DictWin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('b.ico'))
        self.setWindowTitle('主窗口')
        self.action_about.triggered.connect(self.about_event)

    # 菜单栏的关于函数
    def about_event(self):
        QMessageBox.about(self, '关于我们', '这是一个pyqt写成的gui')


# 直接运行 测试上述代码
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_dia = Login()   # 实例化登录窗口
    login_dia.show()
    # dict_win = DictWin()  # 由于login界面有一个dict_win对象，故不需要在程序实例化；主程序实例化只适合在同一个文件
    app.exec_()
