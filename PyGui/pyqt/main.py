# -*- coding: utf-8 -*-
# python的gui编程

import sys
import logging

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from util.logger import console_logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from resource.login_ui import Ui_Dialog
from resource.dict_ui import Ui_MainWindow

# 打印日志信息
logger = console_logging(logging.DEBUG)


class Login(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('b.ico'))
        self.login_btn.clicked.connect(self.end_event)  # 绑定登陆函数
        # self.about_action.triggered.connect(self.about_event)

    # 登陆函数
    def end_event(self):
        if self.name_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入姓名')
        elif self.pwd_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入密码')
        else:
            QMessageBox.information(self, '登陆', self.name_edit.text() + ' 欢迎登陆')
            logger.debug("退出程序")
            # self.accept()     # 加入对话框退出时的返回值
            self.close()  # 关闭登录窗口
            dict_win.show()   # 显示主窗口

    # 菜单栏的关于函数
    def about_event(self):
        QMessageBox.about(self, '关于我们', '这是一个pyqt写成的gui')

    # 键盘按下esc键退出登录界面
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


class DictWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DictWin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('b.ico'))
        self.setWindowTitle('主窗口')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_dia = Login()   # 实例化登录窗口
    login_dia.show()
    # if app.exec_() == QtGui.QDialog.Accepted:
    dict_win = DictWin()  # 实例化主窗口
    sys.exit(app.exec_())

