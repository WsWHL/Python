#! /usr/bin/env python
# -*- coding:utf-8 -*-

from Application import *

if __name__ == "__main__":
    app = Application()
    app.master.title("Tk应用程序")
    # 主消息循环
    app.mainloop()
