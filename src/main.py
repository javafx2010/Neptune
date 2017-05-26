#!/usr/local/bin/python3
from src.javafx.file import file_scaner
from src.javafx.log import logger
from src.javafx.file import file_writer

if __name__ == "__main__":
    log = logger.Logger("/Users/javafx/Work")
    writer = file_writer.FileWriter("/Volumes/XiaoMi/one", log)
    scaner = file_scaner.FileScaner("/Volumes/XiaoMi/图片/home", writer)

    counter = scaner.scan()
    print(counter)
