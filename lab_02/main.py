from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QPixmap, QBrush, QPolygonF
from PyQt6.QtCore import QPointF, Qt
import numpy as np
import sys
import modules.layout as layout
import math

INDENT = 40
TEXT_INDENT = [-20, -10]
NUMBER_OF_POINTS = 50
PARABOLA_WIDTH_COEF = 3
PARABOLA_MAX = 9999

class MainWindow(QMainWindow, layout.Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exitButton.clicked.connect(self.exitApp)
        self.rowCount = 0
        self.clearLabel()
        self.paintButton.clicked.connect(self.changeSetup)
        self.rotateButton.clicked.connect(self.rotateEvt)
        self.moveButton.clicked.connect(self.moveEvt)
        self.resizeButton.clicked.connect(self.rescaleEvt)
        self.resetButton.clicked.connect(self.setup)
        self.turnbackButton.clicked.connect(self.turnback)
        self.circle = QPolygonF()
        self.parabola = QPolygonF()
        self.intersection = QPolygonF()
        self.point = QPointF()
        self.reversed_history = []
        self.setup()

    def setup(self):
        a = b = c = d = 0
        r = 50
        self.reversed_history = []
        self.aForm.setText(str(a))
        self.bForm.setText(str(b))
        self.cForm.setText(str(c))
        self.dForm.setText(str(d))
        self.rForm.setText(str(r))
        self.pointXForm.setText('0')
        self.pointYForm.setText('0')

        self.point = QPointF(self.paintLabel.width() / 2, self.paintLabel.height() / 2)
        self.parabola = self.setupParabola(a, b, c, d, r)
        self.circle = self.setupCircle(360, r, self.paintLabel.width() / 2 + a, self.paintLabel.height() / 2 - b)
        self.intersection = self.circle.intersected(self.parabola)

        self.draw()

    def draw(self):
        self.clearLabel()

        painter = QPainter()
        pixmap = self.paintLabel.pixmap()
        painter.begin(pixmap)

        blackPen = QPen(QColor('black'))
        redPen = QPen(QColor('red'))
        greenPen = QPen(QColor('green'))
        redPenBold = QPen(QColor('red'))
        redPenBold.setWidth(4)
        bluePen = QPen(QColor('blue'))

        blueBrush = QBrush(QColor('blue'), Qt.BrushStyle.SolidPattern)
        painter.setPen(blackPen)
        painter.drawPolygon(self.parabola)

        painter.setPen(redPen)
        painter.drawPolygon(self.circle)
        painter.setPen(bluePen)
        painter.setBrush(blueBrush)
        painter.drawPolygon(self.intersection)

        painter.setPen(redPen)
        pointText = QPointF(self.point.x() - 20, self.point.y() + 30)
        painter.drawText(pointText, "({}, {})".format(self.point.x() - self.paintLabel.width() / 2, self.paintLabel.height() / 2 - self.point.y() ))
        painter.setPen(redPenBold)
        painter.drawPoint(self.point)
        
        painter.setPen(greenPen)
        painter.drawLine(QPointF(0, self.paintLabel.height() / 2),QPointF(self.paintLabel.width(), self.paintLabel.height() / 2))
        painter.drawLine(QPointF(self.paintLabel.width() / 2, 0),QPointF(self.paintLabel.width() / 2, self.paintLabel.height()))
        painter.end()
        self.paintLabel.setPixmap(pixmap)
    
    def changeSetup(self):
        a = self.aForm.text()
        b = self.bForm.text()
        c = self.cForm.text()
        d = self.dForm.text()
        r = self.rForm.text()

        x = self.pointXForm.text()
        y = self.pointYForm.text()
        try:
            a, b, c, d, r = float(a), float(b), float(c), float(d), float(r)
        except:
            self.logErrorIncorrectData()
            a = b = c = d = r = ''
        
        try:
            x, y = float(x), float(y)
        except:
            self.logErrorIncorrectData()
            x = y = ''
        
        if a != '' and x != '':
            self.parabola = self.setupParabola(a, b, c, d, r)
            self.circle = self.setupCircle(360, r, self.paintLabel.width() / 2 + a, self.paintLabel.height() / 2 - b)
            self.intersection = self.circle.intersected(self.parabola)
            self.point = QPointF(self.paintLabel.width() / 2 + x, self.paintLabel.height() / 2 - y)
            self.draw()
            self.reversed_history = []

    def setupParabola(self, a, b, c, d, r):
        halfsize_x = self.paintLabel.width() / 2
        halfsize_y = self.paintLabel.height() / 2

        parabola = QPolygonF()
        
        x = a + r + PARABOLA_MAX - 1
        y = math.sqrt(x - c) + d
        while x < a + r + PARABOLA_MAX:
            x = c + math.pow(y - d, 2)
            parabola.append(QPointF(halfsize_x + x, halfsize_y - (y * PARABOLA_WIDTH_COEF - d)))
            y -= 1
        
        return parabola
    
    def setupCircle(self, n, r, x_pos, y_pos):
        polygon = QPolygonF()
        w = 360 / n
        for i in range(n):
            t = w * i
            x = r * math.cos(math.radians(t))
            y = r * math.sin(math.radians(t))
            polygon.append(QPointF(x_pos + x, y_pos + y))  

        return polygon
    
    def rotateEvt(self):
        alpha = self.rotateForm.text()
        x_axis = self.pointXForm.text()
        y_axis = self.pointYForm.text()
        try:
            alpha = math.radians(float(alpha))
            x_axis = float(x_axis)
            y_axis = float(y_axis)
        except:
            alpha = ''
            self.logErrorIncorrectData()
        if alpha != '':
            self.reversed_history.append([self.rotate, -alpha, x_axis, y_axis])
            self.parabola = self.rotate(self.parabola, alpha, x_axis, y_axis)
            self.circle = self.rotate(self.circle, alpha, x_axis, y_axis)
            self.intersection = self.circle.intersected(self.parabola)
            self.point = QPointF(self.paintLabel.width() / 2 + x_axis, self.paintLabel.height() / 2 - y_axis)
            self.draw()
        
    def rotate(self, polygon: QPolygonF, alpha: float, x_axis: float, y_axis: float):
        center_x = self.paintLabel.width() / 2
        center_y = self.paintLabel.height() / 2
        result_polygon = QPolygonF()
        x_axis += center_x
        y_axis = center_y - y_axis
        
        if alpha != '':
            matrix_A = np.matrix([  
                                    [1      , 0         , 0],
                                    [0      , 1         , 0], 
                                    [-x_axis, -y_axis   , 1]
                                ])
            matrix_B = np.matrix([  
                                    [math.cos(alpha)    , math.sin(alpha)   , 0],
                                    [-math.sin(alpha)   , math.cos(alpha)   , 0], 
                                    [0                  , 0                 , 1]
                                ])
            matrix_C = np.matrix([
                                    [1      , 0     , 0],
                                    [0      , 1     , 0],
                                    [x_axis , y_axis, 1]
                                ])
            result_matrix = np.dot(np.dot(matrix_A, matrix_B), matrix_C)
            for i in range(polygon.count()): 
                point = polygon.value(i)
                result = np.array([point.x(), point.y(), 1])
                result = np.dot(result, result_matrix)
                result_polygon.append(QPointF(result.item(0), result.item(1)))
            
            return result_polygon

    def rescaleEvt(self):
        kx = self.resizeXForm.text()
        ky = self.resizeYForm.text()
        x_axis = self.pointXForm.text()
        y_axis = self.pointYForm.text()
        try:
            kx = float(kx)
            ky = float(ky)
            x_axis = float(x_axis)
            y_axis = float(y_axis)
        except:
            kx = ''
            self.logErrorIncorrectData()
        if kx == 0 or ky == 0:
            self.logErrorIncorrectData()
            kx = ''
        if kx != '':
            self.reversed_history.append([self.rescale, 1/kx, 1/ky, x_axis, y_axis])
            self.parabola = self.rescale(self.parabola, kx, ky, x_axis, y_axis)
            self.circle = self.rescale(self.circle, kx, ky, x_axis, y_axis)
            self.intersection = self.circle.intersected(self.parabola)
            self.point = QPointF(self.paintLabel.width() / 2 + x_axis, self.paintLabel.height() / 2 - y_axis)
            self.draw()

    def rescale(self, polygon: QPolygonF, kx: float, ky: float, x_axis: float, y_axis: float):
        center_x = self.paintLabel.width() / 2
        center_y = self.paintLabel.height() / 2
        result_polygon = QPolygonF()
        x_axis += center_x
        y_axis = center_y - y_axis
        matrix_A = np.matrix([  
                                [1      , 0         , 0],
                                [0      , 1         , 0], 
                                [-x_axis, -y_axis   , 1]
                            ])
        matrix_B = np.matrix([  
                                [kx, 0, 0],
                                [0, ky, 0], 
                                [0, 0,  1]
                            ])
        matrix_C = np.matrix([
                                [1      , 0     , 0],
                                [0      , 1     , 0], 
                                [x_axis , y_axis, 1]
                            ])
        result_matrix = np.dot(np.dot(matrix_A, matrix_B), matrix_C)
        for i in range(polygon.count()):
            point = polygon.value(i)
            result = np.array([point.x(), point.y(), 1])
            result = np.dot(result, result_matrix)
            result_polygon.append(QPointF(result.item(0), result.item(1)))
        
        return result_polygon

    def moveEvt(self):
        x = self.moveXForm.text()
        y = self.moveYForm.text()
        x_axis = self.pointXForm.text()
        y_axis = self.pointYForm.text()
        try:
            x = float(x)
            y = -float(y)
            x_axis = float(x_axis)
            y_axis = float(y_axis)
        except:
            x = ''
            self.logErrorIncorrectData()
        if x != '':
            self.reversed_history.append([self.move, -x, -y])
            self.parabola = self.move(self.parabola, x, y)
            self.circle = self.move(self.circle, x, y)
            self.intersection = self.circle.intersected(self.parabola)
            self.point = QPointF(self.paintLabel.width() / 2 + x_axis, self.paintLabel.height() / 2 - y_axis)
            self.draw()

    def move(self, polygon: QPolygonF, x: float, y: float):
        result_polygon = QPolygonF()
        matrix = np.matrix([  
                                [1, 0, 0],
                                [0, 1, 0], 
                                [x, y, 1]
                            ])
        for i in range(polygon.count()): 
            point = polygon.value(i)           
            result = np.array([point.x(), point.y(), 1])
            result = np.dot(result, matrix)
            result_polygon.append(QPointF(result.item(0), result.item(1)))
        
        return result_polygon

    def turnback(self):
        if self.reversed_history != []:
            oper = self.reversed_history.pop()

            self.parabola = oper[0](self.parabola, *(oper[1:]))
            self.circle = oper[0](self.circle, *(oper[1:]))
            self.intersection = self.circle.intersected(self.parabola)
            self.draw()
            
        else:
            self.logEmptyHistory()

    def logErrorIncorrectData(self):
        self.loggerLabel.setText("!!!ERROR!!! Неверный ввод.")

    def logEmptyHistory(self):
        self.loggerLabel.setText("!!!ERROR!!! История пуста.")

    def logErrorPointExists(self):
        self.loggerLabel.setText("!!!ERROR!!! Точка уже существует.")

    def logErrorInvalidData(self):
        self.loggerLabel.setText("!!!ERROR!!! Точки не подходят под условие задачи.")

    def logErrorPointNotExists(self):
        self.loggerLabel.setText("!!!ERROR!!! Точка не существует.")

    def logErrorInsufficientPoints(self):
        self.loggerLabel.setText("!!!ERROR!!! Недостаточно точек.")

    def logAddPoint(self, n):
        self.loggerLabel.setText("Точка {} добавлена.".format(n))

    def logDeletePoint(self, n):
        self.loggerLabel.setText("Точка {} удалена.".format(n))

    def logDeleteAll(self):
        self.loggerLabel.setText("Все точки удалены.")

    def logSolve(self):
        self.loggerLabel.setText("Решение выведено на экран.")

    def logChangePoint(self, n):
        self.loggerLabel.setText("Точка {} изменена.".format(n))

    def clearLabel(self):
        canvas = QPixmap(self.paintLabel.width(), self.paintLabel.height())
        canvas.fill()
        self.paintLabel.setPixmap(canvas)

    def exitApp(self):
        sys.exit()


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()


