# -*- coding: utf-8 -*-
# python的gui编程

from PyQt5 import QtWidgets
import sys
from gui import Ui_MainWindow

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(dialog)
	dialog.show()
	sys.exit(app.exec())