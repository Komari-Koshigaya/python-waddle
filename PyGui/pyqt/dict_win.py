#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Author :        NIEJUN 
# Datetime：      2020/8/27 8:33
# IDE:            PyCharm
# File Name：     dict_win.py
# DESCRIP：  主界面的处理逻辑

import sys
import logging
from PyQt5.QtGui import QIcon
from util.logger import console_logging
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from resource.dict_ui import Ui_MainWindow

# 打印日志信息
logger = console_logging(logging.DEBUG)


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
        logger.debug("点击了关于.")
        QMessageBox.about(self, '关于我们', '这是一个pyqt写成的gui')

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QMessageBox.question(self,
                                     '本程序',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
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
