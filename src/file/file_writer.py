import shutil

class FileWriter:
    def __init__(self, path,log):
        print(path)
        self.path = path
        self.log=log


    def put(self, file, tag):
        exts = file.split(".")[-1]
        if len(exts) > 0:
            exts = "." + exts
        dist = self.path + "/" + tag + exts
        shutil.copy(file, dist)
        self.log.d(file + "->" + tag)
