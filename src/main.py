#!/usr/local/bin/python3

from src.javafx.analysis import analysiser
from src.javafx.file import file_scaner
from src.javafx.log import logger

if __name__ == "__main__":
    log = logger.Logger("/Users/javafx/Work")
    writer = analysiser.Analysiser("/Users/javafx/Work", log)
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/sony", writer)
    counter = scaner.scan()
    print(counter)
