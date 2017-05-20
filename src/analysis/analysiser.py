import os
from time import gmtime, strftime

class Analysiser:

    def __init__(self, path,log):
        print(path)
        self.path = path
        self.log=log


    def put(self, file, tag):
        exts = file.split(".")[-1]
        ctime=os.path.getctime(file)
        self.log.d(file+"\t"+tag+"\t"+exts+"\t"+str(int(ctime)))