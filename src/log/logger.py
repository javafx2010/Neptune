from time import gmtime, strftime

class Logger:

    def __init__(self,path):
        path=path+"/"+strftime("%Y-%m-%d-%H-%M-%S", gmtime())+".log"
        print("log on\t"+path)
        self.file=open(path,"w")

    def d(self,line):
        print(line)
        self.file.write(line)
        self.file.flush()

    def close(self):
        self.file.close()
