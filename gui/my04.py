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
        self.button01 = Button(root, text="登录",command=self.login)
        self.button01.pack()
        # self.label02 = Label(self, text="百战程序员", width=10, height=2, bg="blue", fg="white",
        #                      font=("黑体", 30))
        self.button01.pack()
        # 显示图像
        global photo
        photo = PhotoImage(file="imgs/logo.PNG")
        self.button03 = Button(root, image=photo, command=self.login)
        self.button03.pack()
        self.button03.config(state = "disabled")

        # self.label04 = Label(self, text="北京\n百战\n赛开",
        #                      borderwidth=1, relief="solid", justify="right")
        # self.label04.pack()
    def login(self):
       messagebox.showinfo("欢迎使用赛开", "登录成功")



root = Tk()
root.geometry("400x600+200+300")
root.title("lable")
app = Application(master=root)

root.mainloop()