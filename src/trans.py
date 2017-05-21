#!/usr/local/bin/python3

from javafx.file import file_scaner
from javafx.log import  logger
from src.javafx.analysis import file_exchange
from src.javafx.file import file_loader

if __name__ == "__main__":
    log = logger.Logger("/Users/javafx/Work/dist")
    loader=file_loader.FileLoader()
    exchange=file_exchange.FileExchange(loader)
    scaner=file_scaner.FileScaner("/Users/javafx/Work/dist", exchange)
    scaner.scan()
