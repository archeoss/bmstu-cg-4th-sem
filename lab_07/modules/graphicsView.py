from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QColor, QPixmap, QPainter
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
        
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.setScene(scene)
        
        print(self.scene().height(), self.backgroundPixmap.height(), self.linesPixmap.height())    
        self.clear()
        
        # height, width = int(self.scene().height()), int(self.scene().width())
        # self.backgroundPixmap = self.backgroundPixmap.scaled(width, height)
        # self.cutterPixmap = self.cutterPixmap.scaled(width, height)
        # self.linesPixmap = self.linesPixmap.scaled(width, height)
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
                    self.linesPixmap = self.drawLine(self.linesPixmap, *self.lastLinePoint, x, y, self.lineColor)
                    self.lines.append([*self.lastLinePoint, x, y])
                    self.lastLinePoint = []
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
            x1, y1 = event.pos().x(), event.pos().y()
            x1, x2, y1, y2 =    min(x1, self.lastCutterPoint[0]),\
                                max(x1, self.lastCutterPoint[0]),\
                                min(y1, self.lastCutterPoint[1]),\
                                max(y1, self.lastCutterPoint[1]),
            self.cutter = [x1, x2 - 1, y2, y1]
    
            self.lastCutterPoint = []
            
        return super().mouseReleaseEvent(event)
    
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.lastCutterPoint != []:
            self.point = event.pos()
            x, y = self.point.x(), self.point.y()
            self.cutterPixmap = QPixmap(int(self.scene().width()), int(self.scene().height()))
            painter = QPainter()
            self.cutterPixmap.fill(QColor("transparent"))
            self.drawRect(self.cutterPixmap, *self.lastCutterPoint, x, y, self.cutterColor)
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
    
    def drawLine(self, pixmap : QPixmap, xa, ya, xb, yb, color):
        # noinspection PyTypeChecker
        painter = QPainter()
        painter.begin(pixmap)
        painter.setPen(QColor(*color))
        points = bresenhamInt(xa, ya, xb, yb)
        for i in points:
            painter.drawLine(i[0], i[1], i[0], i[1])
        # painter.drawLine(round(xa), round(ya), round(xb), round(yb))
        painter.end()
        self.show()
        return pixmap

    def clear(self):
        self.lastLinePoint = []
        self.lastCutterPoint = []
        self.cutter = []
        self.lines = []
    
        height, width = int(self.scene().height()), int(self.scene().width())

        self.backgroundPixmap = QPixmap(width, height)
        self.backgroundPixmap.fill(QColor("black"))
        
        self.linesPixmap = QPixmap(width, height)
        self.linesPixmap.fill(QColor("transparent"))
        
        self.cutterPixmap = QPixmap(width, height)
        self.cutterPixmap.fill(QColor("transparent"))
        self.update(self.backgroundPixmap, self.linesPixmap, self.cutterPixmap)
                    
    def drawRect(self, pixmap, xa, ya, xb, yb, color):
        self.drawLine(pixmap, xa, ya, xa, yb, color)
        self.drawLine(pixmap, xa, ya, xb, ya, color)
        self.drawLine(pixmap, xb, ya, xb, yb, color)
        self.drawLine(pixmap, xa, yb, xb, yb, color)
      
      
      
      
      
      
      
      
        
    def meme(self):
        '''
            ))))))000))00)))0))00))
        '''
        painter = QPainter(self.linesPixmap)
        painter.setPen(QColor('black'))
        painter.fillRect(self.cutter[0], self.cutter[3], self.cutter[1] - self.cutter[0], self.cutter[2] - self.cutter[3], QColor('black'))
        painter.end()
    