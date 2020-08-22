#!/usr/bin/env python3爬虫开发
# -*- coding:utf-8 -*-
# File Name：     picGUI.py
# Author :        NIEJUN 
# Datetime：      2019.11.19 09:05
# IDE:            PyCharm


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import threading


class MyDialog(Toplevel):
    def __init__(self, values):
        super().__init__()
        self.title('Http代理')
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        width = 530
        height = 355
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(size)
        # 弹窗界面
        self.setup_UI()

    def setup_UI(self):
        fram = Frame(self)
        fram.pack()
        self.label = StringVar()
        self.label.set("代理地址：")
        Label(fram, textvariable=self.label).grid(row=0, sticky='W', pady=5)
        self.text = Text(fram, width=60, height=20)
        self.text.grid(row=1)
        self.button = Button(fram, text="确定", command=self.thread_method, width=15, height=1)
        self.button.grid(row=2, column=0, pady=5)

    def thread_method(self):
        t = threading.Thread(target=self.ok)
        t.start()

    def ok(self):
        self.proxy_value = self.text.get('0.0', END)
        self.destroy()  # 销毁窗口



# 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('标题')
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        #设置界面宽度为530，高度为365像素，并且基于屏幕居中
        width = 530
        height = 365
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.master.geometry(size)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        Label(self, text="").grid(row=0, pady=5, columnspan=3)

        self.srcLanguage = StringVar()
        Label(self, text="源语言：").grid(row=1, column=0, sticky='W', pady=5)
        languages = ('en', 'zh-CN', 'zh-TW', 'ja')
        ttk.Combobox(self, values=languages, width=6, textvariable=self.srcLanguage, state='readonly').grid(row=1, column=1,
                                                                                                            sticky='W')

        self.destLanguage = StringVar()
        Label(self, text="目标语言：").grid(row=1, column=1, sticky='E', padx=80)
        ttk.Combobox(self, values=languages, width=6, textvariable=self.destLanguage, state='readonly').grid(row=1,
                                                                                                             column=1,
                                                                                                             sticky='E',
                                                                                                             padx=0)

        self.interval = StringVar()
        Label(self, text="请求间隔(s)：").grid(row=3, sticky='W', pady=5)
        Entry(self, textvariable=self.interval, width=9).grid(row=3, column=1, sticky='W')

        self.proxy = StringVar()
        self.proxyValues = []
        Label(self, text="Http代理：").grid(row=4, sticky='W', pady=5)
        Checkbutton(self, variable=self.proxy).grid(row=4, column=1, sticky='W', padx=0)
        Button(self, text=" 配置 ", command=self.openProxyFram).grid(row=4, column=1, sticky='W', padx=30)
        self.proxy.set(1)

        self.excludeKey = StringVar()
        Label(self, text="不翻译属性：").grid(row=5, sticky='W', pady=5)
        Entry(self, textvariable=self.excludeKey, width=40).grid(row=5, column=1, sticky='W')
        Label(self, text="（多个用,分隔）").grid(row=5, column=2, columnspan=2, sticky='W')

        self.htmlKey = StringVar()
        Label(self, text="Html标签属性：").grid(row=6, sticky='W', pady=5)
        Entry(self, textvariable=self.htmlKey, width=40).grid(row=6, column=1, sticky='W')
        Label(self, text="（多个用,分隔）").grid(row=6, column=2, columnspan=2, sticky='W')

        Label(self, text="输入文件夹：").grid(row=7, column=0, sticky='W', pady=5)
        self.inDirectory = StringVar()
        Entry(self, textvariable=self.inDirectory, width=40).grid(row=7, column=1, sticky='W')
        Button(self, text=" ... ", command=self.selectPath).grid(row=7, column=2, sticky='W', padx=2)

        Label(self, text="输出文件夹：").grid(row=8, column=0, sticky='W', pady=5)
        self.outDirectory = StringVar()
        Entry(self, textvariable=self.outDirectory, width=40).grid(row=8, column=1, sticky='W')
        Button(self, text=" ... ", command=self.selectPath2).grid(row=8, column=2, sticky='W', padx=2)

        self.translateButton = Button(self, text="批量翻译", command=self.translate, height=2, width=20)
        self.translateButton.grid(row=9, columnspan=3, padx=10, pady=10)

        Button(self, text="停止", command=self.destroy, height=2, width=10).grid(row=9, columnspan=3, padx=50, sticky='E')

        self.pause_str = StringVar()
        self.pause_str.set('暂停')
        Button(self, textvariable=self.pause_str, command=self.pause_method, height=2, width=10).grid(row=9, columnspan=3,
                                                                                                      padx=50, sticky='W')
    def translate(self):
        print("tanslate json!\n")

    def pause_method(self):
        print("tanslate json!\n")

    def selectPath(self):
        self.inDirectory.set(askdirectory())

    def selectPath2(self):
        self.inDirectory.set(askdirectory())

    def openProxyFram(self):
        inputDialog = MyDialog(self.proxyValues)
        self.wait_window(inputDialog)
        if hasattr(inputDialog,'proxy_value'):
            proxy_value = inputDialog.proxy_value.strip()


app = Application()
app.mainloop()

def sayHello():
    print("helloworld!\n")