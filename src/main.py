from src.file import file_scaner

if __name__ == "__main__":
    scaner = file_scaner.FileScaner("/Users/javafx/Git", ".py")
    scaner.scan()
