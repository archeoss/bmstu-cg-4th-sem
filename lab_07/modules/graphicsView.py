from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QColor, QPixmap, QPainter
from more_itertools import last
from .basic_func import bresenhamInt


class GraphicsView(QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)
        self.lastLinePoint = []
        self.lastCutterPoint = []
        self.cutter = []
        self.lineColor = []
        self.resultColor = []
        self.cutterColor = []
        self.lines = []
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.setScene(scene)

        height, width = int(self.scene().height()), int(self.scene().width())

        self.backgroundPixmap = QPixmap(width, height)
        self.backgroundPixmap.fill(QColor("black"))
        
        self.linesPixmap = QPixmap(width, height)
        self.linesPixmap.fill(QColor("transparent"))
        
        self.cutterPixmap = QPixmap(width, height)
        self.cutterPixmap.fill(QColor("transparent"))
        self.update(self.backgroundPixmap, self.linesPixmap, self.cutterPixmap)
        
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        # self.clear()
        
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.setScene(scene)
        height, width = int(self.scene().height()), int(self.scene().width())
        self.backgroundPixmap = self.backgroundPixmap.scaled(width, height)
        self.cutterPixmap = self.cutterPixmap.scaled(width, height)
        self.linesPixmap = self.linesPixmap.scaled(width, height)
        print(self.scene().height(), self.backgroundPixmap.height(), self.linesPixmap.height())    
        self.update(self.backgroundPixmap, self.linesPixmap, self.cutterPixmap)
    
        return super().resizeEvent(event)
    
    def mousePressEvent(self, event):
        self.point = event.pos()
        x, y = self.point.x(), self.point.y()
        painter = QPainter()
        match event.button(): 
            case Qt.MouseButton.LeftButton:
                if self.lastLinePoint != []:
                    painter.begin(self.linesPixmap)
                    painter.setPen(QColor(*self.lineColor))
                    painter.drawLine(*self.lastLinePoint, x, y)
                    self.lines.append([*self.lastLinePoint, x, y])
                    self.lastLinePoint = []
                    painter.end()
                else:
                    self.lastLinePoint = [x, y]
                    
            case Qt.MouseButton.RightButton:
                if self.lastCutterPoint != []:
                    
                    self.lastCutterPoint = []
                else:
                    self.lastCutterPoint = [x, y]
        
        self.update(self.backgroundPixmap, self.linesPixmap, self.cutterPixmap)
        
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.lastCutterPoint != []:
            self.lastCutterPoint = []
        return super().mouseReleaseEvent(event)
    
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.lastCutterPoint != []:
            self.point = event.pos()
            x, y = self.point.x(), self.point.y()
            self.cutterPixmap = QPixmap(int(self.scene().width()), int(self.scene().height()))
            painter = QPainter()
            self.cutterPixmap.fill(QColor("transparent"))
            painter.begin(self.cutterPixmap)
            painter.setPen(QColor(*self.cutterColor))
            self.drawRect(*self.lastCutterPoint, x, y, painter)
            painter.end()
            self.update(self.backgroundPixmap, self.linesPixmap, self.cutterPixmap)
            
        return super().mouseMoveEvent(event)
    
    def update(self, backgroundPixmap, linesPixmap, cutterPixmap):
        scene = self.scene()
        scene.clear()
        scene.addPixmap(backgroundPixmap)
        scene.addPixmap(linesPixmap)
        scene.addPixmap(cutterPixmap)
        self.setScene(scene)
        
    def paintEvent(self, event):
        super().paintEvent(event)
    
    def drawLine(self, xa, ya, xb, yb, color):
        # noinspection PyTypeChecker
        points = bresenhamInt(xa, ya, xb, yb)
        for i in points:
            self.scene().addLine(i[0], i[1], i[0], i[1], QColor(*color))
        self.show()

    def clear(self):
        self.lastLinePoint = []
        self.lastCutterPoint = []
        self.cutter = []
        self.lines = []
        self.lineColor = []
        self.resultColor = []
        self.cutterColor = []
        
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.setScene(scene)

        height, width = int(self.scene().height()), int(self.scene().width())

        self.backgroundPixmap = QPixmap(width, height)
        self.backgroundPixmap.fill(QColor("black"))
        
        self.linesPixmap = QPixmap(width, height)
        self.linesPixmap.fill(QColor("transparent"))
        
        self.cutterPixmap = QPixmap(width, height)
        self.cutterPixmap.fill(QColor("transparent"))
        self.update(self.backgroundPixmap, self.linesPixmap, self.cutterPixmap)
                    
    def drawRect(self, xa, ya, xb, yb, painter : QPainter):
        painter.drawLine(xa, ya, xa, yb)
        painter.drawLine(xa, ya, xb, ya)
        painter.drawLine(xb, ya, xb, yb)
        painter.drawLine(xa, yb, xb, yb)