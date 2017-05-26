#-*-conding:utf-8-*-
import os
import codecs
from src.javafx.image import classif


class FileScaner:
    def __init__(self, path, writer):
        self.path = path
        self.writer = writer

    charset="UTF-8"

    def load(self,path):
        if os.path.exists(path):
            file = codecs.open(path, "r", self.charset)
            ls = file.readlines()
            for i in range(len(ls)):
                ls[i] = ls[i].replace("\n", "")
                print(ls[i])
            file.close()
            self.lines = ls
        else:
            self.lines=[]

    def skip(self,path):
        lines=self.lines
        for i in range(len(lines)):
            if lines[i] == path:
                return 1
        return 0

    def scan(self):
        counter = 0

        self.load(self.path+"/../process")

        process=codecs.open(self.path+"/../process","w",self.charset)
        class_if = classif.classif()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if os.path.isfile(os.path.join(root, file)):
                    full_path = os.path.join(root, file)
                    if self.skip(full_path)==1:
                        print("skip:\t"+full_path)
                        continue
                    self.writer.put(full_path)
                    process.write(full_path+"\n")
                    process.flush()

                    counter += 1

        self.writer.flush()
        process.close()
        return counter

