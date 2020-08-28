# -*- coding: utf-8 -*-
# python的gui编程

# 主程序，先出现登录界面，登录成功则跳转到主界面
if __name__ == '__main__':
    import sys
    from login_dialog import LoginDialog

    try:
        from PyQt5.QtWidgets import QApplication
    except ModuleNotFoundError as e:
        # 执行时引入 pyqt5库失败时，则使用 pip指令安装
        import os
        print('本机未安装pyqt，正在安装 PyQt5 ...')
        os.system(
            'pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn pyqt5')

    app = QApplication(sys.argv)
    login_dia = LoginDialog()  # 实例化登录窗口
    login_dia.show()
    app.exec_()
