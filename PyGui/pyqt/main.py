# -*- coding: utf-8 -*-
# python的gui编程

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.end_event)  # 绑定登陆函数
        self.actionabout.triggered.connect(self.about_event)

    # 登陆函数
    def end_event(self):
        if self.name_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入姓名')
        elif self.pwd_edit.text() == "":
            QMessageBox.about(self, '登陆', '请输入密码')
        else:
            QMessageBox.information(self, '登陆', self.name_edit.text() + ' 欢迎登陆')

    # 菜单栏的关于函数
    def about_event(self):
        QMessageBox.about(self, '关于我们', '这是一个pyqt写成的gui')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
