#!/usr/local/bin/python3

from javafx.file import file_scaner
from javafx.log import  logger
from javafx.analysis import analysiser

if __name__ == "__main__":
    log=logger.Logger("/Users/javafx/Work/dist")
    writer = analysiser.Analysiser("/Users/javafx/Work/dist",log)
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/home/文档", writer)
    counter = scaner.scan()
    print(counter)
