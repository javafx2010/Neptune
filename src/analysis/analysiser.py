

class Analysiser:

    def __init__(self, path,log):
        print(path)
        self.path = path
        self.log=log


    def put(self, file, tag):
        self.log.d(file+"\t"+tag)