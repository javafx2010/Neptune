import shutil
from javafx.image import  classif

class FileWriter:
    def __init__(self, path,log):
        print(path)
        self.path = path
        self.log=log
        self.class_if=classif.classif()


    def put(self, file):
        tag = self.class_if.action(file)
        exts = file.split(".")[-1]
        if len(exts) > 0:
            exts = "." + exts
        dist = self.path + "/" + tag + exts
        shutil.copy(file, dist)
        self.log.d(file + "->" + dist)
