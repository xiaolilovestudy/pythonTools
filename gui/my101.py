"""测试Canvas组件的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox
import random



class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):

        self.label01 = Label(self, text="用户名")
        self.label01.grid(column=0, row=0)
        self.entry01 = Entry(self).grid(column=1, row=0)

        self.label02 = Label(self, text="密码").grid(column=0, row=1)
        self.entry02 = Entry(self, show="*").grid(column=1, row=1)

        Label(self, text="用户名为手机号").grid(column=2, row=0)

        Button(self, text="登录").grid(rowspan=2, column=1, sticky=EW)
        Button(self, text="取消").grid(row=2, column=2, sticky=EW)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()