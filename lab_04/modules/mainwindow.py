from PyQt6.QtWidgets import QMainWindow, QWidget, QGraphicsScene
from PyQt6.QtGui import QColor, QPixmap, QPolygonF
from PyQt6.QtCore import QPointF
import sys
import os
from .layout import *
from .draw import *
from .plot import *

class MainWindow(QMainWindow, Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.color = [255, 0, 0]
        self.curAlgo = 'lib'
        self.curFigure = 'circle'
        self.setupUi(self)
        self.connectButtons()

        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)

        self.pixmap = QPixmap(int(scene.width()), int(scene.height()))
        self.pixmap.fill(QColor('black'))
        scene.addPixmap(self.pixmap)

        self.graphicsView.setScene(scene)

        scene2 = QGraphicsScene()
        self.graphicsView_2.setScene(scene2)
        scene2.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)

        scene3 = QGraphicsScene()
        self.graphicsView_3.setScene(scene3)
        scene3.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)

        self.rowCount = 0
        self.circle = QPolygonF()
        self.parabola = QPolygonF()
        self.intersection = QPolygonF()
        self.point = QPointF()
        self.reversed_history = []

    def drawClicked(self):
        x = self.centerXForm.text()
        y = self.centerYForm.text()
        r_a = self.radius_aForm.text()
        if self.curFigure == 'ellipse':
            r_b = self.radius_bForm.text()
        else:
            r_b = r_a
        try:
            x, y, r_a, r_b = float(x), float(y), float(r_a), float(r_b)
        except:
            self.logErrorIncorrectData()
            x = y = r_a = ''
        if x != '':
            draw(self.pixmap, self.color, x, y, r_a, r_b, self.curAlgo, self.curFigure)
            self.graphicsView.scene().addPixmap(self.pixmap)

    def drawSunClicked(self):
        r_a = self.radius_aSunForm.text()
        amount = self.amountForm.text()
        step = self.stepForm.text()
        x = self.centerSunXForm.text()
        y = self.centerSunYForm.text()
        if self.curFigure == 'ellipse':
            r_b = self.radius_bSunForm.text()
        else:
            r_b = r_a
        try:
            r_a, r_b, amount, step, x, y = float(r_a), float(r_b), int(amount), float(step), float(x), float(y) 

        except:
            self.logErrorIncorrectData()
            step = r = amount = 0
        if step > 0 and r_a >= 0 and amount > 0:
            error = drawSun(self.pixmap, self.color, x, y, r_a, r_b, amount, step, self.curAlgo, self.curFigure)
            if (error):
                self.clear()
                self.logErrorDrawError()
            else:
                self.graphicsView.scene().addPixmap(self.pixmap)

    def analysis(self):
        self.graphicsView_2.scene().clear()
        self.graphicsView_3.scene().clear()
        makePlot()
        self.graphicsView_2.scene().addPixmap(QPixmap(PLOT_CIRCLE_PATH))
        self.graphicsView_3.scene().addPixmap(QPixmap(PLOT_ELLIPSE_PATH))

    def setRed(self):
        self.color = [255, 0, 0]
    def setBlue(self):
        self.color = [0, 0, 255]
    def setWhite(self):
        self.color = [255, 255, 255]
    def setBlack(self):
        self.color = [0, 0, 0]

    def setLib(self):
        self.curAlgo = 'lib'
    def setCanonic(self):
        self.curAlgo = 'canonical'
    def setParametric(self):
        self.curAlgo = 'parametric'
    def setBrez(self):
        self.curAlgo = 'bresenham'
    def setMidPoint(self):
        self.curAlgo = 'midPoint'

    def setCircle(self):
        self.curFigure = 'circle'
        self.r2Label.setDisabled(True)
        self.r2SunLabel.setDisabled(True)
        self.radius_bForm.setDisabled(True)
        self.radius_bSunForm.setDisabled(True)
    def setEllipse(self):
        self.curFigure = 'ellipse'
        self.r2Label.setDisabled(False)
        self.r2SunLabel.setDisabled(False)
        self.radius_bForm.setDisabled(False)
        self.radius_bSunForm.setDisabled(False)

    def connectButtons(self):
        self.exitButton.clicked.connect(self.exitApp)
        self.exitButton_2.clicked.connect(self.exitApp)
        self.drawButton.clicked.connect(self.drawClicked)
        self.drawSunButton.clicked.connect(self.drawSunClicked)
        self.resetButton.clicked.connect(self.clear)
        self.analysisButton.clicked.connect(self.analysis)

        self.circleButton.clicked.connect(self.setCircle)
        self.ellipseButton.clicked.connect(self.setEllipse)

        self.redButton.clicked.connect(self.setRed)
        self.blueButton.clicked.connect(self.setBlue)
        self.whiteButton.clicked.connect(self.setWhite)
        self.blackButton.clicked.connect(self.setBlack)

        self.libAlgoButton.clicked.connect(self.setLib)
        self.canonAlgoButton.clicked.connect(self.setCanonic)
        self.paramAlgoButton.clicked.connect(self.setParametric)
        self.brezAlgoButton.clicked.connect(self.setBrez)
        self.midPointAlgoButton.clicked.connect(self.setMidPoint)

    def logErrorIncorrectData(self):
        self.loggerLabel.setText("!!!ERROR!!! Неверный ввод.")

    def logErrorDrawError(self):
        self.loggerLabel.setText("!!!ERROR!!! Во время отоброжения произошла ошибка. \n Возможно неверный алгоритм")

    def logErrorInsufficientPoints(self):
        self.loggerLabel.setText("!!!ERROR!!! Недостаточно точек.")

    def logSolve(self):
        self.loggerLabel.setText("Решение выведено на экран.")

    def clear(self):
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)
        self.pixmap = QPixmap(int(scene.width()), int(scene.height()))
        self.pixmap.fill(QColor('black'))
        scene.addPixmap(self.pixmap)

        self.graphicsView.setScene(scene)

    def exitApp(self):
        sys.exit()
