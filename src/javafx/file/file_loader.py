

class FileLoader:


    def scan(self,path):
        file=open(path,"rt",encoding='utf-8')
        lines=file.readlines()
        file.close()
        return lines
