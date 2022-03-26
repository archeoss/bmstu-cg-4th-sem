from PyQt6.QtGui import QPixmap, QPainter, QColor
from .algorithms.dda import *
from PyQt6.QtCore import QPointF
from math import sin, cos, radians
from .algorithms.bresenham import *
from .algorithms.wu import *

MAX_ANGLE = 360

def draw(pixmap : QPixmap, pcolor : list[int], \
            x1 : float, y1 : float, x2 : float, y2 : float, algo : str):
    center_x = pixmap.width() / 2
    center_y = pixmap.height() / 2
    painter = QPainter()
    painter.begin(pixmap)
    painter.setPen(QColor(*pcolor, 255))
    skip = False
    error = False
    func = None
    match algo:
        case 'lib':
            painter.drawLine(QPointF(center_x + x1 , center_y - y1), QPointF(center_x + x2, center_y - y2))
            skip = True
        case 'dda':
            func = dda
        case 'brezFloat':
            func = breisenhamFloat
        case 'brezInt':
            func = breisenhamInt
        case 'brezAA':
            func = breisenhamAA
        case 'wu':
            func = Wu
        case _:
            error = True
            skip = True
    
    if not skip:
        points = func((center_x + x1), (center_y - y1), (center_x + x2), (center_y - y2))
        for i in points:
            x, y = i[0], i[1]
            painter.setPen(QColor(*pcolor, i[2]))
            painter.drawPoint(QPointF(x, y))
    painter.end()
    
    return error

def drawSun(pixmap : QPixmap, pcolor : list[int], rad : float, step : float, algo : str):    
    angle = 0
    center_x = center_y = 0
    while (angle < MAX_ANGLE):
        x = sin(radians(angle)) * rad
        y = cos(radians(angle)) * rad
        angle += step
        error = draw(pixmap, pcolor, center_x, center_y, x, y, algo)    
        if error != 0:
            break
    
    return error

    