#!/usr/local/bin/python3

from javafx.file import file_scaner
from javafx.file import  file_writer
from javafx.log import  logger

if __name__ == "__main__":
    log = logger.Logger("/Users/javafx/Work/dist")
    writer=file_writer.FileWriter("/Users/javafx/Work/target",log)
    scaner=file_scaner.FileScaner("/Users/javafx/Work/dist", writer)
