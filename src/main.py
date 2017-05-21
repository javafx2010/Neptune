#!/usr/local/bin/python3

from javafx.file import file_scaner
from javafx.log import  logger
from javafx.file import file_writer

if __name__ == "__main__":
    log=logger.Logger("/Volumes/XiaoMi/图片/dist")
    writer = file_writer.FileWriter("/Volumes/XiaoMi/图片/dist",log)
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/home", writer)
    counter = scaner.scan()
    print(counter)
