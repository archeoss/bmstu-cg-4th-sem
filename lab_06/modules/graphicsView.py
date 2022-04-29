from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtGui import QColor
from .basic_func import bresenhamInt


class GraphicsView(QGraphicsView):
    def __init__(self, *args):
        super().__init__(*args)
        self.points = []
        self.bordColor = []
        self.fillColor = []
        self.lastColored = None
        self.point = None
        self.isNew = True
        self.prefilledPoints = []
        self.start_point = []
        
    def mousePressEvent(self, event):
        self.point = event.pos()
        match event.button():
            case Qt.MouseButton.MiddleButton:
                self.prefilledPoints.append([self.point.x(),  self.point.y()])
                self.drawPrefilled()            
            case Qt.MouseButton.LeftButton:
                if self.isNew:
                    self.points.append([])
                    self.points[-1].append([self.point.x(), self.point.y()])
                    self.isNew = False
                    self.start_point = [self.point.x(), self.point.y()]
                else:
                    self.points[-1].append([self.point.x(), self.point.y()])
                self.draw()
            case Qt.MouseButton.RightButton:
                if not self.isNew:
                    self.points[-1].append([self.start_point[0], self.start_point[1]])
                    self.start_point = []
                    self.draw()
                    self.isNew = True

    def mouseReleaseEvent(self, event):
        self.point = None

    def paintEvent(self, event):
        super().paintEvent(event)
        
    def drawPrefilled(self):
        # noinspection PyTypeChecker
        self.scene().addLine(*self.prefilledPoints[-1], *self.prefilledPoints[-1], QColor(*(self.fillColor)))
        self.show()
    
    def draw(self):
        # noinspection PyTypeChecker
        self.scene().addLine(*self.points[-1][-1], *self.points[-1][-1], QColor(*(self.bordColor)))
        if len(self.points[-1]) > 1 and not self.isNew:
            points = bresenhamInt(*(self.points[-1][-1]), *(self.points[-1][-2]))
            for i in points:
                self.scene().addLine(i[0], i[1], i[0], i[1], QColor(*(self.bordColor)))
        self.show()
