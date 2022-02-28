from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QPixmap
from PyQt6.QtCore import QPointF, QLineF
import sys
import modules.layout as layout
import math

INDENT = 40
TEXT_INDENT = [30, 0]

class MainWindow(QMainWindow, layout.Ui_Dialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addPointButton.clicked.connect(self.addPoint)
        self.deleteAllButton.clicked.connect(self.deleteAll)
        self.deletePointButton.clicked.connect(self.deletePoint)
        self.changePointButton.clicked.connect(self.changePoint)
        self.exitButton.clicked.connect(self.exitApp)
        self.rowCount = 0
        self.points = []
        self.clearLabel()
        self.solveButton.clicked.connect(self.solve)
    
    def solve(self):
        '''
            В треугольнике для наибольшей высоты соответствует наименьшая сторона этого треугольника.
            Поэтому для решения задачи необходимо найти наибольшую сторону среди наименьших сторон треугольников
        '''
        self.clearLabel()
        result_idxs = []
        all_max_side = -1
        if len(self.points) > 2:
            for i in range(len(self.points)):
                for j in range(i + 1, len(self.points)):
                    for k in range(j + 1, len(self.points)):
                        side_a = math.sqrt(math.pow(self.points[i][0] - self.points[j][0], 2) + math.pow(self.points[i][1] - self.points[j][1], 2))
                        side_b = math.sqrt(math.pow(self.points[i][0] - self.points[k][0], 2) + math.pow(self.points[i][1] - self.points[k][1], 2))
                        side_c = math.sqrt(math.pow(self.points[j][0] - self.points[k][0], 2) + math.pow(self.points[j][1] - self.points[k][1], 2))
                        min_side = min(side_a, side_b, side_c)
                        if all_max_side < min_side and (side_a + side_b > side_c and side_c + side_a > side_b and side_c + side_b > side_a):
                            all_max_side = min_side
                            result_idxs = [i, j, k]
            if result_idxs == []:
                self.logErrorInvalidData()
            else:
                if side_c >= side_a <= side_b:
                    x_real, y_real = self.orthoProjection(self.points[result_idxs[0]], self.points[result_idxs[1]], self.points[result_idxs[2]])
                elif side_c >= side_b <= side_a:
                    x_real, y_real = self.orthoProjection(self.points[result_idxs[0]], self.points[result_idxs[2]], self.points[result_idxs[1]])
                elif side_a >= side_c <= side_b:
                    x_real, y_real = self.orthoProjection(self.points[result_idxs[1]], self.points[result_idxs[2]], self.points[result_idxs[0]])
                self.points.append([x_real, y_real])
                self.drawResult(result_idxs)
                self.points.pop()
                self.logSolve()
        else:
            self.logErrorInsufficientPoints()

    def drawResult(self, result_idxs):
        painter = QPainter()
        pixmap = self.paintLabel.pixmap()
        painter.begin(pixmap)
        pen = QPen()
        pen2 = QPen()
        pen3 = QPen()
        pen.setColor(QColor('red'))
        pen2.setColor(QColor('red'))
        pen3.setColor(QColor('blue'))
        pen.setWidth(3)
        pen2.setWidth(3)
        pen3.setWidth(3)
        pen2.setDashPattern([5,5])
        pen2.setDashOffset(5)
        painter.setPen(pen)
        if len(self.points) > 2:
            halfsize_x = self.paintLabel.width() / 2
            halfsize_y = self.paintLabel.height() / 2
            x_min, y_min, x_max, y_max = self.edge_coords(self.points)
            center_x = (x_max + x_min) / 2
            center_y = (y_max + y_min) / 2
            coef = min((halfsize_x - INDENT)/(abs(center_x - x_min)), (halfsize_y - INDENT)/(abs(center_y - y_min)))
            
            result_points = []
            for i in range(3):
                x = halfsize_x + (self.points[result_idxs[i]][0] - center_x) * coef
                y = halfsize_y - (self.points[result_idxs[i]][1] - center_y) * coef
                result_points.append([x, y])

            side_a = math.sqrt(math.pow(result_points[0][0] - result_points[1][0], 2) + math.pow(result_points[0][1] - result_points[1][1], 2))
            side_b = math.sqrt(math.pow(result_points[0][0] - result_points[2][0], 2) + math.pow(result_points[0][1] - result_points[2][1], 2))
            side_c = math.sqrt(math.pow(result_points[1][0] - result_points[2][0], 2) + math.pow(result_points[1][1] - result_points[2][1], 2))
            painter.setPen(pen3)
            if side_c >= side_a <= side_b:
                x, y = self.orthoProjection(result_points[0], result_points[1], result_points[2])
                painter.drawLine(QLineF(result_points[2][0], result_points[2][1], x, y))
                painter.setPen(pen2)
                painter.drawLine(QLineF(result_points[1][0], result_points[1][1], x, y))
                painter.setPen(pen)
            elif side_c >= side_b <= side_a:
                x, y = self.orthoProjection(result_points[0], result_points[2], result_points[1])
                painter.drawLine(QLineF(result_points[1][0], result_points[1][1], x, y))
                painter.setPen(pen2)
                painter.drawLine(QLineF(result_points[0][0], result_points[0][1], x, y))
                painter.setPen(pen)
            elif side_a >= side_c <= side_b:
                x, y = self.orthoProjection(result_points[1], result_points[2], result_points[0])
                painter.drawLine(QLineF(result_points[0][0], result_points[0][1], x, y))
                painter.setPen(pen2)
                painter.drawLine(QLineF(result_points[1][0], result_points[1][1], x, y))
                painter.setPen(pen)
            painter.setPen(pen)
            painter.drawLine(QLineF(result_points[0][0], result_points[0][1], result_points[1][0], result_points[1][1]))
            painter.drawLine(QLineF(result_points[0][0], result_points[0][1], result_points[2][0], result_points[2][1]))
            painter.drawLine(QLineF(result_points[1][0], result_points[1][1], result_points[2][0], result_points[2][1]))
             
        else:
            self.logErrorInsufficientPoints()
        painter.end()
        self.paintLabel.setPixmap(pixmap)
        self.drawPoints()

    def drawPoints(self):
        painter = QPainter()
        pixmap = self.paintLabel.pixmap()
        painter.begin(pixmap)
        pen = QPen()
        if len(self.points) > 2:
            halfsize_x = self.paintLabel.width() / 2
            halfsize_y = self.paintLabel.height() / 2
            x_min, y_min, x_max, y_max = self.edge_coords(self.points)
            center_x = (x_max + x_min) / 2
            center_y = (y_max + y_min) / 2
            coef = min((halfsize_x - INDENT)/(abs(center_x - x_min)), (halfsize_y - INDENT)/(abs(center_y - y_min)))
            
            pen.setColor(QColor('black'))
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawLine(QPointF(halfsize_x + (0 - center_x) * coef, 0), QPointF(halfsize_x + (0 - center_x) * coef, self.paintLabel.height()))
            painter.drawText(QPointF(halfsize_x + (0 - center_x) * coef + 10, 10), "y")

            painter.drawLine(QPointF(0, halfsize_y - (0 - center_y) * coef), QPointF(self.paintLabel.width(), halfsize_y - (0 - center_y) * coef))
            painter.drawText(QPointF(self.paintLabel.width() - 10, halfsize_y - (0 - center_y) * coef + 10), "x")
 
            pen.setColor(QColor('red'))
            pen.setWidth(3)
            painter.setPen(pen)
            
            for i in range(len(self.points)):
                print(halfsize_x + (self.points[i][0] - center_x) * coef, halfsize_y + (self.points[i][1] - center_y) * coef)
                x = halfsize_x + (self.points[i][0] - center_x) * coef
                y = halfsize_y - (self.points[i][1] - center_y) * coef
                painter.drawPoint(QPointF(x, y))
                if i != len(self.points) - 1:
                    painter.drawText(QPointF(x + TEXT_INDENT[0], y + TEXT_INDENT[1]), "{}: {};{}".format(i + 1, self.points[i][0], self.points[i][1]))
                else:
                    painter.drawText(QPointF(x + TEXT_INDENT[0], y + TEXT_INDENT[1]), "{}: {:g};{:g}".format("h", self.points[i][0], self.points[i][1]))
 
        else:
            self.logErrorInsufficientPoints()
        painter.end()
        self.paintLabel.setPixmap(pixmap)
        
    def edge_coords(self, points):
        if points != []:
            x_max = x_min = points[0][0]
            y_max = y_min = points[0][1]
            for i in range(1, len(points)):
                x_max = max(points[i][0], x_max)
                y_max = max(points[i][1], y_max)
                x_min = min(points[i][0], x_min)
                y_min = min(points[i][1], y_min)
        
        return x_min, y_min, x_max, y_max
        
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
                self.logAddPoint(self.rowCount)
                self.clearLabel()
    
    def deleteAll(self):
        self.rowCount = 0
        self.tableOfPoints.setRowCount(self.rowCount)
        self.points = []
        self.logDeleteAll()
        self.clearLabel()

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
            self.logDeletePoint(n + 1)
            self.clearLabel()
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
                self.logChangePoint(n + 1)
                self.clearLabel()
        else:
            self.logErrorIncorrectData()

    def orthoProjection(self, point_a, point_b, point_height):
        abx = point_b[0] - point_a[0]
        aby = point_b[1] - point_a[1]
        acx = point_height[0] - point_a[0]
        acy = point_height[1] - point_a[1]
        t = (abx * acx + aby * acy) / (abx * abx + aby * aby)
        px = point_a[0] + t * abx
        py = point_a[1] + t * aby

        return px, py

    def logErrorIncorrectData(self):
        self.loggerLabel.setText("!!!ERROR!!! Неверный ввод.")

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
