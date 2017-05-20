import os

from src.image import classif


class FileScaner:
    def __init__(self, path, exts, writer):
        self.path = path
        self.exts = exts
        self.writer = writer

    def scan(self):
        counter = 0
        class_if = classif.classif()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.exts):
                    tag = class_if.action(file)
                    self.writer.put(file, tag)
                    counter += 1
        return counter
