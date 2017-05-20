from src.file import file_scaner
from src.file import file_writer

if __name__ == "__main__":
    writer = file_writer.FileWriter("/Volumes/XiaoMi/TDDOWNLOAD")
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/home", ".JPG", writer)
    scaner.scan()
