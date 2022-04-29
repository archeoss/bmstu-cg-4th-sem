from PyQt6.QtWidgets import QMainWindow, QWidget, QColorDialog, QGraphicsScene
from PyQt6.QtGui import QColor, QPixmap
import sys
from .layout import Ui_Dialog
from .draw import fill_polygon
# from .plot import


class MainWindow(QMainWindow, Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.bordColor = self.graphicsView.bordColor = [255, 0, 0]
        self.fillColor = self.graphicsView.fillColor = [0, 0, 255]
        self.isDelay = False
        self.connectButtons()

        self.pointYForm.setText(str())
        self.pointXForm.setText("400")

        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)

        self.pixmap = QPixmap(int(scene.width()), int(scene.height()))
        self.pixmap.fill(QColor('black'))
        scene.addPixmap(self.pixmap)

        self.graphicsView.setScene(scene)

        scene2 = QGraphicsScene()
        self.graphicsView_2.setScene(scene2)
        scene2.setSceneRect(0, 0, self.mainFrame.width() - 10, self.mainFrame.height() - 10)

    def mousePressEvent(self, event):
        # Вызов перерисовки виджета
        self.graphicsView.update()

    def enclose(self):
        self.graphicsView.points[-1].append(self.graphicsView.start_point)
        self.graphicsView.draw()
        self.graphicsView.isNew = True

    def drawClicked(self):
        self.isDelay = self.delayButton.isChecked()
        delay_time = self.delaySlider.maximum() - self.delaySlider.value() + 1 if self.isDelay else 0
        fill_polygon(self.graphicsView, self.fillColor, self.bordColor, self.isDelay, delay_time)
    
    def addPoint(self):
        x = self.pointXForm.text()
        y = self.pointYForm.text()
        try:
            x, y = int(x), int(y)
        except ValueError:
            self.logErrorIncorrectData()
            x = y = ''
        if x != '':
            if self.graphicsView.isNew:
                self.graphicsView.isNew = False
                self.graphicsView.points.append([])
                self.graphicsView.start_point = [x, y]
            self.graphicsView.points[-1].append([x, y])
            self.graphicsView.draw()

    def analysis(self):
        self.graphicsView_2.scene().clear()
        # makePlot()
        # self.graphicsView_2.scene().addPixmap(QPixmap(PLOT_PATH))
        
    def chooseBorderColor(self):
        dialog = QColorDialog()
        self.bordColor = list(dialog.getColor().getRgb()[:-1])
        self.graphicsView.bordColor = self.bordColor
        self.borderColorLabel.setStyleSheet("background-color: rgb(%d, %d, %d);"
                                            % (self.bordColor[0], self.bordColor[1], self.bordColor[2]))

    def chooseFillColor(self):
        dialog = QColorDialog()
        self.fillColor = list(dialog.getColor().getRgb()[:-1])
        self.graphicsView.fillColor = self.fillColor
        self.fillColorLabel.setStyleSheet("background-color: rgb(%d, %d, %d);"
                                          % (self.fillColor[0], self.fillColor[1], self.fillColor[2]))

    def connectButtons(self):
        self.exitButton.clicked.connect(self.exitApp)
        self.exitButton_2.clicked.connect(self.exitApp)
        self.drawButton.clicked.connect(self.drawClicked)
        self.resetButton.clicked.connect(self.clear)
        self.analysisButton.clicked.connect(self.analysis)
        self.addPointButton.clicked.connect(self.addPoint)
        
        self.encloseButton.clicked.connect(self.enclose)

        self.fillColorButton.clicked.connect(self.chooseFillColor)
        self.borderColorButton.clicked.connect(self.chooseBorderColor)

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
