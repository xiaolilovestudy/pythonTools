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
        self.canvas = Canvas(self, width=300, height=300, bg="green")
        self.canvas.pack()

        # 画直线
        line = self.canvas.create_line(10,20,30,40,50,60)
        # 画矩形
        rect = self.canvas.create_rectangle(40,40, 80,80)
        # 画圆
        oval = self.canvas.create_oval(40,40,80,80)

        global  photo
        photo = PhotoImage(file="imgs/logo.PNG")
        self.canvas.create_image(150, 170,image=photo)

        Button(self, text="画10个矩形", command=self.draw10Recg).pack(side="left")

    def draw10Recg(self):
        for x in range(0,10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = y1 + random.randrange(int(self.canvas["height"])/2)
            self.canvas.create_rectangle(x1,y1, x2,y2)

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()