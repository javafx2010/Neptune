import os


class FileScaner:
    def __init__(self, path, exts):
        self.path = path
        self.exts = exts

    def scan(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.exts):
                    print(os.path.join(root, file))
