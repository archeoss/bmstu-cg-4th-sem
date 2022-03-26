from PyQt6.QtWidgets import QMainWindow, QWidget, QGraphicsScene
from PyQt6.QtGui import QColor, QPixmap, QPolygonF
from PyQt6.QtCore import QPointF
import sys
from .layout import *
from .draw import *
from .plot import *

INDENT = 40
TEXT_INDENT = [-20, -10]
NUMBER_OF_POINTS = 50
PARABOLA_WIDTH_COEF = 3
PARABOLA_MAX = 9999

HIST_PATH = os.path.join(os.path.dirname(__file__), 'plots/histo.png')
PLOT_PATH = os.path.join(os.path.dirname(__file__), 'plots/plot.png')

class MainWindow(QMainWindow, Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.color = [255, 0, 0]
        self.curAlgo = 'lib'
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
#    def setup(self):
        
    def drawClicked(self):
        x1 = self.point_aXForm.text()
        x2 = self.point_bXForm.text()
        y1 = self.point_aYForm.text()
        y2 = self.point_bYForm.text()
        
        try:
            x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)
        except:
            self.logErrorIncorrectData()
            x1 = x2 = y1 = y2 = ''
        if x1 != '':
            draw(self.pixmap, self.color, x1,y1,x2,y2, self.curAlgo)
            self.graphicsView.scene().addPixmap(self.pixmap)

    def drawSunClicked(self):
        r = self.radiusForm.text()
        step = self.stepForm.text()

        try:
            r, step = float(r), float(step)
        except:
            self.logErrorIncorrectData()
            step = r = 0
        if step > 0 and r > 0:
            error = drawSun(self.pixmap, self.color, r, step, self.curAlgo)
            if (error):
                self.clear()
                self.logErrorDrawError()
            else:
                self.graphicsView.scene().addPixmap(self.pixmap)

    def analysis(self):
        self.graphicsView_2.scene().clear()
        self.graphicsView_3.scene().clear()
        makePlot()
        self.graphicsView_2.scene().addPixmap(QPixmap(HIST_PATH))
        self.graphicsView_3.scene().addPixmap(QPixmap(PLOT_PATH))

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
    def setDDA(self):
        self.curAlgo = 'dda'
    def setBrezFloat(self):
        self.curAlgo = 'brezFloat'
    def setBrezInt(self):
        self.curAlgo = 'brezInt'
    def setBrezAA(self):
        self.curAlgo = 'brezAA'
    def setWu(self):
        self.curAlgo = 'wu'

    def connectButtons(self):
        self.exitButton.clicked.connect(self.exitApp)
        self.exitButton_2.clicked.connect(self.exitApp)
        self.drawButton.clicked.connect(self.drawClicked)
        self.drawSunButton.clicked.connect(self.drawSunClicked)
        self.resetButton.clicked.connect(self.clear)
        self.analysisButton.clicked.connect(self.analysis)

        self.redButton.clicked.connect(self.setRed)
        self.blueButton.clicked.connect(self.setBlue)
        self.whiteButton.clicked.connect(self.setWhite)
        self.blackButton.clicked.connect(self.setBlack)

        self.libAlgoButton.clicked.connect(self.setLib)
        self.ddaAlgoButton.clicked.connect(self.setDDA)
        self.brezFloatAlgoButton.clicked.connect(self.setBrezFloat)
        self.brezIntAlgoButton.clicked.connect(self.setBrezInt)
        self.brezAAAlgoButton.clicked.connect(self.setBrezAA)
        self.wuAlgoButton.clicked.connect(self.setWu)

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
