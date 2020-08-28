#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author :        NIEJUN 
# Datetime：      2020/8/26 8:53
# IDE:            PyCharm
# File Name：     login_dialog.py
# DESCRIP：   登陆界面的控制逻辑

import sys
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from dict_win import DictWin
from util.logger import console_logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from resource.login_ui import Ui_Dialog

# 打印日志信息
logger = console_logging(logging.DEBUG)


class LoginDialog(QMainWindow, Ui_Dialog):
    """
    登录界面的控制逻辑
    """

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.dict_win = DictWin()  # 实例化一个主窗口界面
        self.setupUi(self)
        self.setWindowIcon(QIcon('b.ico'))
        self.login_btn.setStyleSheet('''color: white; background-color: rgb(218,181,150);''')
        self.regi_btn.setStyleSheet('''color: white; background-color: rgb(218,181,150);''')

        """
        绑定函数有两种写法 
        1. self.login_btn.clicked.connect( lambda: self.login_event('argument') )  可以传参，推荐使用
        2. self.login_btn.clicked.connect(self.login_event)  无法传参，login_event()也不能有self之外的参数，否则会报错
        """
        # self.login_btn.clicked.connect(self.login_event)  # 使用方法二 绑定登陆函数
        self.login_btn.clicked.connect(lambda: self.login_event(name='小小怪'))  # 使用方法一 绑定登陆函数

    def login_event(self, name):
        """
        点击登录时，进行登录验证
        :return: None
        """
        logger.info("触发登录事件，并传递了参数：" + name)
        if self.name_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入姓名')
        elif self.pwd_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入密码')
        else:
            QMessageBox.information(self, '登陆', self.name_edit.text() + ' 欢迎登陆')
            logger.debug(self.name_edit.text() + "登录成功，将退出登录界面，跳转到主界面！")
            # dict_win = DictWin()

            self.dict_win.show(self.name_edit.text())  # 显示主窗口, 并传递登录的用户名
            self.close()  # 关闭登录窗口

    def keyPressEvent(self, e):
        """
        键盘按下esc键退出登录界面
        :param e:
        :return: None
        """
        if e.key() == Qt.Key_Escape:
            self.close()


# 直接运行 测试上述代码
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_dia = LoginDialog()  # 实例化登录窗口
    login_dia.show()
    # dict_win = DictWin()  # 由于login界面有一个dict_win对象，故不需要在程序实例化；主程序实例化只适合在同一个文件
    app.exec_()
