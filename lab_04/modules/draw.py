from PyQt6.QtGui    import QPixmap, QPainter, QColor
from PyQt6.QtCore   import QPointF, QPoint
from math           import sin, cos, radians

from .algorithms.canonical  import *
from .algorithms.parametric import *
from .algorithms.bresenham  import *
from .algorithms.midpoint   import *

def draw(pixmap : QPixmap, pcolor : list[int, 3], \
            x : float, y : float, r_a : float, r_b : float,\
                algo : str, figure : str):
    painter = QPainter()
    painter.begin(pixmap)
    painter.setPen(QColor(*pcolor, 255))
    skip = False
    error = False
    func = None
    match figure:
        case 'circle':
            match algo:
                case 'lib':
                    painter.drawEllipse(QPointF(x, y), r_a, r_b)
                    skip = True
                case 'canonical':
                    func = canonical_circle
                case 'parametric':
                    func = parcircle
                case 'bresenham':
                    func = brescircle
                case 'midPoint':
                    func = midpcircle
                case _:
                    error = True
                    skip = True
        case 'ellipse':
            match algo:
                case 'lib':
                    painter.drawEllipse(QPointF(x, y), r_a, r_b)
                    skip = True
                case 'canonical':
                    func = canonical_ellipse
                case 'parametric':
                    func = parellipse
                case 'bresenham':
                    func = bresellipse
                case 'midPoint':
                    func = midpellipse
                case _:
                    error = True
                    skip = True
        case _:
            error = True
            skip = True

    if not skip:
        match figure:
            case 'circle':
                points = func(x, y, r_a, 255)
            case 'ellipse':
                points = func(x, y, r_a, r_b, 255)
        for i in points:
            x, y = i[0], i[1]
            painter.setPen(QColor(*pcolor, i[2]))
            painter.drawPoint(QPoint(x, y))
    painter.end()
    
    return error

def drawSun(pixmap : QPixmap, pcolor : list[int], x : float, y : float, r_a : float, r_b : float, amount : int, step : float, algo : str, figure : str):    
    cur_n = 0
    while cur_n < amount:
        cur_n += 1
        r_a += step
        r_b += step
        error = draw(pixmap, pcolor, x, y, r_a, r_b, algo, figure)
        if error != 0:
            break
    
    return error

    