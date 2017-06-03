#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Base(object):
    """基类"""

    def __init__(self):
        self.name = 'Base'
        self.run()

    def run(self):
        print('基类的Run方法，当前name值为：', self.name)


class ChildA(Base):
    """子类A"""

    def __init__(self):
        super().__init__()
        self.name = 'ChildA'
        self.run()

    def run(self):
        print('子类A的Run方法，当前name值为：', self.name)

class ChildB(ChildA):
    """子类B"""

    def __init__(self):
        super().__init__()
        self.name = 'ChildB'
        self.run()

    def run(self):
        print('子类B的Run方法，当前name值为：', self.name)

if __name__ == '__main__':
    c = ChildB()
