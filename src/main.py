from src.file import file_scaner
from src.file import file_writer
from src.log import  logger

if __name__ == "__main__":
    log=logger.Logger("/Volumes/XiaoMi/TDDOWNLOAD")
    writer = file_writer.FileWriter("/Volumes/XiaoMi/TDDOWNLOAD",log)
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/home", writer)
    counter = scaner.scan()
    print(counter)
