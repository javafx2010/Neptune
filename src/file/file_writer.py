import shutil

class FileWriter:
    def __init__(self, path):
        print(path)
        self.path = path

    def put(self, file, tag):
        exts = file.split(".")[-1]
        if len(exts) > 0:
            exts = "." + exts
        dist = self.path + "/" + tag + exts
        shutil.copy(file, dist)
        print(file + "->" + tag)
