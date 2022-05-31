from PyQt6.QtWidgets import QMainWindow, QWidget, QColorDialog, QGraphicsScene
from PyQt6.QtGui import QColor, QPixmap
import sys

from .graphicsView import GraphicsView
from .layout import Ui_Dialog
from .draw import clipping

class MainWindow(QMainWindow, Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lineColor = self.graphicsView.lineColor = [255, 255, 255]
        self.resultColor = self.graphicsView.resultColor = [255, 0, 0]
        self.cutterColor = self.graphicsView.cutterColor = [0, 0, 255]
        
        self.isDelay = False
        self.connectButtons()

    def drawClicked(self):
        self.graphicsView.meme()
        clipping(self.graphicsView)
        
    def addLine(self):
        xa = self.lineXAForm.text()
        ya = self.lineYAForm.text()
        xb = self.lineXBForm.text()
        yb = self.lineYBForm.text()
        flag = True
        try:
            xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)
        except ValueError:
            self.logErrorIncorrectData()
            flag = False
        if flag:
            self.graphicsView.lines.append([xa, ya, xb, yb])
            self.graphicsView.drawLine(self.graphicsView.linesPixmap, xa, ya, xb, yb, self.lineColor)
            self.graphicsView.update(self.graphicsView.backgroundPixmap, self.graphicsView.linesPixmap, self.graphicsView.cutterPixmap, )
        
    def addCutter(self):
        xa = self.cutterXAForm.text()
        ya = self.cutterYAForm.text()
        xb = self.cutterXBForm.text()
        yb = self.cutterYBForm.text()
        flag = True
        try:
            xa, ya, xb, yb = int(xa), int(ya), int(xb), int(yb)
        except ValueError:
            self.logErrorIncorrectData()
            flag = False
        if flag:
            x1, x2, y1, y2 =    min(xa, xb),\
                                max(xa, xb),\
                                min(ya, yb),\
                                max(ya, yb),
            self.graphicsView.cutter = [x1, x2, y2, y1]
            self.graphicsView.drawRect(self.graphicsView.cutterPixmap, xa, ya, xb, yb, self.cutterColor)
            self.graphicsView.update(self.graphicsView.backgroundPixmap, self.graphicsView.linesPixmap, self.graphicsView.cutterPixmap, )
        
        
    def chooseLineColor(self):
        dialog = QColorDialog()
        self.lineColor = list(dialog.getColor().getRgb()[:-1])
        self.graphicsView.lineColor = self.lineColor
        self.lineColorLabel.setStyleSheet("background-color: rgb(%d, %d, %d);"
                                            % (self.lineColor[0], self.lineColor[1], self.lineColor[2]))

    def chooseResultColor(self):
        dialog = QColorDialog()
        self.resultColor = list(dialog.getColor().getRgb()[:-1])
        self.graphicsView.resultColor = self.resultColor
        self.resultColorLabel.setStyleSheet("background-color: rgb(%d, %d, %d);"
                                          % (self.resultColor[0], self.resultColor[1], self.resultColor[2]))

    def chooseCutterColor(self):
        dialog = QColorDialog()
        self.cutterColor = list(dialog.getColor().getRgb()[:-1])
        self.graphicsView.cutterColor = self.cutterColor
        self.cutterColorLabel.setStyleSheet("background-color: rgb(%d, %d, %d);"
                                          % (self.cutterColor[0], self.cutterColor[1], self.cutterColor[2]))

    def connectButtons(self):
        self.exitButton.clicked.connect(self.exitApp)
        self.cutButton.clicked.connect(self.drawClicked)
        self.resetButton.clicked.connect(self.clear)
        self.addLineButton.clicked.connect(self.addLine)
        self.addCutterButton.clicked.connect(self.addCutter)

        self.resultColorButton.clicked.connect(self.chooseResultColor)
        self.lineColorButton.clicked.connect(self.chooseLineColor)
        self.cutterColorButton.clicked.connect(self.chooseCutterColor)

    def logErrorIncorrectData(self):
        self.loggerLabel.setText("!!!ERROR!!! Неверный ввод.")

    def logErrorDrawError(self):
        self.loggerLabel.setText("!!!ERROR!!! Во время отоброжения произошла ошибка. \n Возможно неверный алгоритм")

    def logErrorInsufficientPoints(self):
        self.loggerLabel.setText("!!!ERROR!!! Недостаточно точек.")

    def logErrorSameColor(self):
        self.loggerLabel.setText("!!!ERROR!!! Цвет заполнения и границ одинаковый\n Смените цвет")

    def logSolve(self):
        self.loggerLabel.setText("Решение выведено на экран.")

    def clear(self):
        self.graphicsView.clear()

    def exitApp(self):
        sys.exit()
