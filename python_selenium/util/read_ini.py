#coding=utf-8
import configparser

class ReadIni(object):
    def __init__(self, filename=None, node=None):
        if filename == None:
            filename = r"D:\pythonTools\python_selenium\LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(filename)

    def load_ini(self, filename):
        cf  = configparser.ConfigParser()
        cf.read(filename)  # D:\pythonTools\python_selenium
        return cf

    def get_value(self, key):

        date = self.cf.get(self.node,key)
        return date


if __name__ == "__main__":
    read_init = ReadIni()
    print(read_init.get_value("code_text"))