from PyQt6.QtWidgets import QMainWindow, QWidget, QColorDialog, QGraphicsScene
from PyQt6.QtGui import QColor, QPixmap
import sys
from .layout import Ui_Dialog

class MainWindow(QMainWindow, Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lineColor = self.graphicsView.lineColor = [255, 255, 255]
        self.resultColor = self.graphicsView.resultColor = [255, 0, 0]
        self.cutterColor = self.graphicsView.cutterColor = [0, 0, 255]
        
        self.isDelay = False
        self.connectButtons()

    def enclose(self):
        self.graphicsView.points[-1].append(self.graphicsView.start_point)
        self.graphicsView.draw()
        self.graphicsView.isNew = True

    def drawClicked(self):
        self.isDelay = self.delayButton.isChecked()
        delay_time = self.delaySlider.maximum() - self.delaySlider.value() + 1 if self.isDelay else 0
        # fill_polygon(self.graphicsView, self.fillColor, self.bordColor, self.isDelay, delay_time)
    
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
            self.graphicsView.drawLine(xa, ya, xb, yb, self.lineColor)
        
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
            self.graphicsView.drawRect(xa, ya, xb, yb, self.cutterColor)
        
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
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)
        self.pixmap = QPixmap(int(scene.width()), int(scene.height()))
        self.pixmap.fill(QColor('black'))
        scene.addPixmap(self.pixmap)
        self.graphicsView.points = []
        self.graphicsView.isNew = True
        self.graphicsView.start_point = []
        self.graphicsView.prefilledPoints = []
        self.graphicsView.setScene(scene)

    def exitApp(self):
        sys.exit()
