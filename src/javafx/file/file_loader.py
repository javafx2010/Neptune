import io

class FileLoader:


    def scan(self,path,callback):

        with io.open(path, 'rb') as f:
            for line in f:
                callback(line)
        f.close()
