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
        self.label01 = Label(self, text="百战", width=10, height=2,bg="black",fg="white" )
        self.label01.pack()
        self.label02 = Label(self, text="百战程序员", width=10, height=2, bg="blue", fg="white",
                             font=("黑体", 30))
        self.label02.pack()
        # 显示图像
        global photo
        photo = PhotoImage(file="imgs/logo.PNG")
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="北京\n百战\n赛开",
                             borderwidth=1, relief="solid", justify="right")
        self.label04.pack()

root = Tk()
root.geometry("400x600+200+300")
root.title("lable")
app = Application(master=root)

root.mainloop()