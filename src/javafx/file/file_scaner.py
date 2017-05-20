import os

from javafx.image import classif


class FileScaner:
    def __init__(self, path, writer):
        self.path = path
        self.writer = writer

    def scan(self):
        counter = 0
        class_if = classif.classif()
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if os.path.isfile(os.path.join(root, file)):
                    full_path = os.path.join(root, file)
                    self.writer.put(full_path)
                    counter += 1
        return counter

