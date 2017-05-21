

class FileExchange:

    def __init__(self,loader):
        self.loader=loader

    def put(self,path):
        self.loader.scan(path,self.callback)

    def callback(self,line):
        print(line)