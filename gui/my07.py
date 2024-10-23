#
from tkinter import *
from tkinter import messagebox

class Application(Frame):
    """一个经典的GUI程序写法"""


    def __init__(self, master = None):
        super().__init__(master) # super()代表父类的定义，而不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""

        self.label01 = Label(self, text="用户名")
        self.label01.pack()

        # StringVar 变量绑定到指定的组件
        # StringVar变量的值发生变化，组件内容也会发生变化
        # 双向关联
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        v1.set("admin")

        # 创建密码框
        self.label02 = Label(self, text="密码")
        self.label02.pack()
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        self.btn01 = Button(root, text="登录", command=self.login)
        self.btn01.pack()

    def login(self):
        username = self.entry01.get()
        password = self.entry02.get()
        print("去数据库比对用户名和密码！")
        print("输入的用户名：", username)
        print("输入的密码：", password)
        if username == "dli5x" and password == "123456":
            messagebox.showinfo("欢迎使用赛开", "登录成功")
        else:
            messagebox.showinfo("登录失败", "用户名或密码不正确")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x600+200+300")
    root.title("欢迎使用赛开登录系统")
    app = Application(master=root)

    root.mainloop()