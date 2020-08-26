# -*- coding: utf-8 -*-
# python的gui编程

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from win_contro import Login, DictWin

# 主程序，先出现登录界面，登录成功则跳转到主界面
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_dia = Login()   # 实例化登录窗口
    login_dia.show()
    app.exec_()



