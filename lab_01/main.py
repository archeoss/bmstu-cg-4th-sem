from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
import modules.layout as layout

class MainWindow(QMainWindow, layout.Ui_Dialog, QTableWidgetItem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addPointButton.clicked.connect(self.addPoint)
        self.deleteAllButton.clicked.connect(self.deleteAll)
        self.deletePointButton.clicked.connect(self.deletePoint)
        self.changePointButton.clicked.connect(self.changePoint)
        self.rowCount = 0
        self.points = []

    def addPoint(self):
        x, y = self.addXForm.text(), self.addYForm.text()
        self.addXForm.setText("")
        self.addYForm.setText("")
        try:
            x = float(x)
            y = float(y)
        except:
            x = y = ''
            self.logErrorIncorrectData()
        
        if x != '':
            if [x, y] in self.points:
                self.logErrorPointExists()
            else:
                self.points.append([x, y])
                self.tableOfPoints.insertRow(self.rowCount)
                self.tableOfPoints.setItem(self.rowCount, 0, QTableWidgetItem(str(x)))
                self.tableOfPoints.setItem(self.rowCount, 1, QTableWidgetItem(str(y)))
                self.rowCount += 1
                self.loggerLabel.setText("Точка {} добавлена.".format(self.rowCount))
    
    def deleteAll(self):
        self.rowCount = 0
        self.tableOfPoints.setRowCount(self.rowCount)
        self.points = []
        self.loggerLabel.setText("Точки удалены.".format(self.rowCount))
    
    def deletePoint(self):
        n = self.deleteNumberForm.text()
        try:
            n = int(n) - 1
        except:
            n = ''
        if n != '' and len(self.points) > n >= 0:
            self.points.pop(n)
            self.rowCount -= 1
            self.tableOfPoints.removeRow(n)
            self.loggerLabel.setText("Точка {} удалена".format(n))
        else:
            self.logErrorIncorrectData()
        
    
    def changePoint(self):
        x, y = self.changeXForm.text(), self.changeYForm.text()
        n = self.changeNumberForm.text()
        try:
            n = int(n) - 1
            x = float(x)
            y = float(y)
        except:
            x = y = n = ''
            self.logErrorIncorrectData()
        if n != '' and len(self.points) > n >= 0:
            if [x, y] in self.points:
                self.logErrorPointExists()
            else:
                self.points[n] = [x, y]
                self.tableOfPoints.setItem(n, 0, QTableWidgetItem(str(x)))
                self.tableOfPoints.setItem(n, 1, QTableWidgetItem(str(y)))
        else:
            self.logErrorIncorrectData()

    def logErrorIncorrectData(self):
        self.loggerLabel.setText("!!!ERROR!!! Неверный ввод.")

    def logErrorPointExists(self):
        self.loggerLabel.setText("!!!ERROR!!! Точка уже существует.")

    def logErrorPointNotExists(self):
        self.loggerLabel.setText("!!!ERROR!!! Точка не существует.")



def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
