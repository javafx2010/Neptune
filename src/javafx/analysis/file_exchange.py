

class FileExchange:

    def __init__(self,loader):
        self.loader=loader

    def put(self,path):
        lines=self.loader.scan(path)
        print(lines)
