from modules.mainwindow import *
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
