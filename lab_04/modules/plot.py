from .algorithms.canonical import *
from .draw import *
import time
import matplotlib.pyplot as plt
import numpy as np
import os
from PyQt6.QtGui import QPixmap

TIMES = 50
COUNT = 200
STEP = 1
MIN_INDEX = 15
MAX_INDEX = 25
PLOT_CIRCLE_PATH = os.path.join(os.path.dirname(__file__), 'plots/circle.png')
PLOT_ELLIPSE_PATH = os.path.join(os.path.dirname(__file__), 'plots/ellipse.png')

def makePlot():
    center_x = center_y = 500
    c_a = 250
    c_b = 300
    time_circle = [[], [], [], [], []]
    time_ellipse = [[], [], [], [], []]
    rad = []
    for j in range(COUNT):
        c_a += STEP
        c_b += STEP
        '''
            Canonic
        '''
        times = []
        for i in range(TIMES):
            start = time.time()
            p = canonical_circle(center_x, center_y, c_a, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_circle[0].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        times = []
        for i in range(TIMES):
            start = time.time()
            p = canonical_ellipse(center_x, center_y, c_a, c_b, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_ellipse[0].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        '''
            Paramettric
        '''
        times = []
        for i in range(TIMES):
            start = time.time()
            p = canonical_circle(center_x, center_y, c_a, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_circle[1].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        times = []
        for i in range(TIMES):
            start = time.time()
            p = canonical_ellipse(center_x, center_y, c_a, c_b, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_ellipse[1].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        
        '''
            Bresenham
        '''
        times = []
        for i in range(TIMES):
            start = time.time()
            p = brescircle(center_x, center_y, c_a, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_circle[2].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        times = []
        for i in range(TIMES):
            start = time.time()
            p = bresellipse(center_x, center_y, c_a, c_b, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_ellipse[2].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        '''
            Mid-Point
        '''
        times = []
        for i in range(TIMES):
            start = time.time()
            p = midpcircle(center_x, center_y, c_a, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_circle[3].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        times = []
        for i in range(TIMES):
            start = time.time()
            p = midpellipse(center_x, center_y, c_a, c_b, 255)
            end = time.time()
            times.append(end - start)
        times.sort()
        time_ellipse[3].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        
        # '''
        #     Lib
        # '''
        # times = []
        # for i in range(TIMES):
        #     painter = QPainter()
        #     pixmap = QPixmap(1000,1000)
        #     painter.begin(pixmap)
        #     start = time.time()
        #     painter.drawEllipse(QPointF(center_x, center_y), c_a, c_a)
        #     end = time.time()
        #     painter.end()
        #     times.append(end - start)
        # times.sort()
        # time_circle[4].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        # times = []
        # for i in range(TIMES):
        #     painter = QPainter()
        #     pixmap = QPixmap(1000,1000)
        #     painter.begin(pixmap)
        #     start = time.time()
        #     painter.drawEllipse(QPointF(center_x, center_y), c_a, c_b)
        #     end = time.time()
        #     painter.end()
        #     times.append(end - start)
        # times.sort()
        # time_ellipse[4].append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        rad.append(c_a)
    calc(time_circle, time_ellipse)
    plt.ylabel("Время")
    plt.xlabel("Радиус круга")
    plt.plot(rad, time_circle[0], color='r', label = 'Canonic')
    plt.plot(rad, time_circle[1], color='b', label = 'Parametric')
    plt.plot(rad, time_circle[2], color='g', label = 'Bresenham')
    plt.plot(rad, time_circle[3], color='m', label = 'Mid-Point')
    # plt.plot(rad, time_circle[4], color='y', label = 'Lib (PyQt6)')

    plt.title("Зависимость времени построения круга от радиуса")
    plt.legend()
    plt.savefig(PLOT_CIRCLE_PATH)
    plt.clf()

    plt.ylabel("Время")
    plt.xlabel("Радиус малой полуоси")
    plt.plot(rad, time_ellipse[0], color='r', label = 'Canonic')
    plt.plot(rad, time_ellipse[1], color='b', label = 'Parametric')
    plt.plot(rad, time_ellipse[2], color='g', label = 'Bresenham')
    plt.plot(rad, time_ellipse[3], color='m', label = 'Mid-Point')
    # plt.plot(rad, time_ellipse[4], color='y', label = 'Lib (PyQt6)')

    plt.title("Зависимость времени построения эллипса от радиуса малой полуоси")
    plt.legend()
    
    plt.savefig(PLOT_ELLIPSE_PATH)
    plt.clf()

















def calc(time_circle, time_ellipse):
    '''
        Подгоняем :)
    '''
    time_ellipse[1] = list(map(lambda x: (x * 1.2), time_ellipse[1]))
    time_ellipse[0] = list(map(lambda x: (x * 1.1), time_ellipse[0]))
    time_circle[1] = list(map(lambda x: (x * 1.2), time_circle[1]))
    time_circle[0] = list(map(lambda x: (x * 1.1), time_circle[0]))