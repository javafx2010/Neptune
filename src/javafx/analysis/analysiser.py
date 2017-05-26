import os

from src.javafx.image import classif


class Analysiser:

    def __init__(self, path,log):
        print(path)
        self.path = path
        self.log=log
        self.class_if = classif.classif()


    def put(self, file):
        tag = self.class_if.action(file)
        exts = file.split(".")[-1]
        if len(exts) <=0:
            exts="invalid"

        ctime=os.path.getctime(file)
        self.log.d(file+"\t"+tag+"\t"+exts+"\t"+str(int(ctime)))