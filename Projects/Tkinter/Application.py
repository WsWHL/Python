#! /usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    """应用程序类"""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.lbName = Label(self, text="Name:", fg="blue")
        self.lbName.grid(row=0, column=0, sticky=W)
        self.txtName = Entry(self)
        self.txtName.grid(row=0, column=1)
        self.btnShow = Button(self, text="Click", command=self.alertMessage)
        self.btnShow.grid(row=1, columnspan=2)

    def alertMessage(self):
        name = self.txtName.get() or "World!"
        messagebox.showinfo(title="温馨提示：", message="Hello，%s" % name)
