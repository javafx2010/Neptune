import shutil

from src.javafx.image import classif
import os
from datetime import datetime

class FileWriter:
    def __init__(self, path,log):
        print(path)
        self.path = path
        self.log=log
        self.class_if=classif.classif()

    def ensure_dir(self,file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def put(self, file):
        tag = self.class_if.action(file)
        file_exts = file.split(".")[-1]
        exts=file_exts
        if len(file_exts) > 0:
            exts = "." + exts
        else:
            file_exts=".default"

        ctime = os.path.getctime(file)
        file_time = datetime.fromtimestamp(ctime).strftime('%Y_%m')
        dist = self.path +"/"+file_exts+ "/"+file_time+"/" + tag + exts
        self.ensure_dir(dist)
        shutil.copy(file, dist)
        self.log.d(file + "->" + dist)

    def flush(self):
        print("over")
