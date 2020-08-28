#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author :        NIEJUN 
# Datetime：      2020/8/27 8:33
# IDE:            PyCharm
# File Name：     dict_win.py
# DESCRIP：  主界面的处理逻辑

import sys
import logging
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from util.logger import console_logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from resource.dict_ui import Ui_MainWindow
import qtawesome

# 打印日志信息
logger = console_logging(logging.DEBUG)


class DictWin(QMainWindow, Ui_MainWindow):
    """
    主界面的控制逻辑
    """
    def __init__(self, parent=None):
        super(DictWin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('b.ico'))
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 使用 qtawesome 这个第三方库来实现按钮中的 Font Awesome字体图标的显示
        self.pushButton.setIcon(qtawesome.icon('fa.music', color='white'))  # 设置按钮的图标
        self.pushButton_left_2.setIcon(qtawesome.icon('fa.download', color='white'))
        self.pushButton_left_3.setIcon(qtawesome.icon('fa.question', color='white'))

        """
        QSS全称为Qt StyleSheet,是用来控制QT控件的样式表。其和Web前段开发中的CSS样式表类似
        通过setStyleSheet()方法，设置按钮部件的QSS样式，左侧按钮默认为淡绿色，鼠标悬浮时为深绿色；
        中间按钮默认为淡黄色，鼠标悬浮时为深黄色；右侧按钮默认为浅红色，鼠标悬浮时为红色
        实例代码   self.frame_nav.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        """
        self.label_user.setStyleSheet('''QLabel{color:white;font-weight:800;}''')
        self.frame_nav.setStyleSheet('''
            QPushButton{
                border:none;
                color:white;
                font-size:15px;
            }
            QPushButton#pushButton_left_2{
                /*700会使字变粗 helvetica 会有下划线*/
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton:hover{
                color:black;
                border-radius:10px;
                background:LightGray;
                border-left:4px solid red;
                font-weight:700;
            }
            QWidget#frame_nav{    
                background:gray;
            }
        ''')
        self.frame_content.setStyleSheet('''
            QWidget#frame_content{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
        ''')

        # 绑定事件
        self.action_about.triggered.connect(self.about_event)

    def about_event(self):
        """
        菜单栏的关于函数
        :return: None
        """
        logger.debug("点击了关于.")
        QMessageBox.about(self, '关于我们', '这是一个pyqt写成的gui')

    def show(self, name='小小怪下士'):
        """
        重写页面显示的 show()方法，以界面跳转时传递的参数
        :param name: 登录的用户名
        :return: None
        """
        super(DictWin, self).show()
        self.label_user.setText(name)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self, '本程序', "是否要退出程序？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            logger.debug("还是决定要退出")
            event.accept()
        else:
            logger.debug("还是不退出了")
            event.ignore()


# 直接运行 测试上述代码
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = DictWin()  # 实例化登录窗口
    main_win.show()
    app.exec_()
