from src.file import file_scaner
from src.log import  logger
from src.analysis import analysiser

if __name__ == "__main__":
    log=logger.Logger("/Users/javafx/Work/dist")
    writer = analysiser.Analysiser("/Users/javafx/Work/dist",log)
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/home", writer)
    counter = scaner.scan()
    print(counter)
