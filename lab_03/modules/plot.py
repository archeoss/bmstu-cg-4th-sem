from .algorithms.bresenham import *
from .algorithms.dda import *
from .algorithms.wu import *
from .draw import *
import time
import matplotlib.pyplot as plt
import numpy as np
import os
from PyQt6.QtGui import QPixmap
from PyQt6 import QtWidgets 

TIMES = 10
TOTAL_DEGREES = 90
RADIUS = 1000
STEP = 1

HIST_PATH = os.path.join(os.path.dirname(__file__), 'plots/histo.png')
PLOT_PATH = os.path.join(os.path.dirname(__file__), 'plots/plot.png')

def makePlot():
    step = STEP
    rad = RADIUS
    angle = 0
    center_x = center_y = 0
    timer = [[], [], [], [], [], []]
    points = []
    steps = [[], [], [], [], []]
    while (angle < TOTAL_DEGREES):
        x = sin(radians(angle)) * rad
        y = cos(radians(angle)) * rad
        times = []
        for i in range(TIMES):
            start = time.time()
            p = dda(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[0].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = breisenhamInt(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[1].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = breisenhamFloat(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[2].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = breisenhamAA(center_x, center_y, x, y)
            end = time.time()
            times.append(end - start)
        timer[3].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = Wu(center_y, center_x, y, x)
            end = time.time()
            times.append(end - start)
        timer[4].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))
        
        times = []
        for i in range(TIMES):
            painter = QPainter()
            pixmap = QPixmap(1000,1000)
            painter.begin(pixmap)
            start = time.time()
            painter.drawLine(QPointF(center_x, center_y), QPointF(x, y))
            end = time.time()
            painter.end()
            times.append(end - start)
        timer[5].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        
        angle += step
    times_b = list(map(lambda x: sum(x) / len(x), timer))
    objects = ['DDA', 'Bres. Int', 'Bres. Float', 'Bres. AA', 'Wu','Lib.Line']
    y_pos = np.arange(len(times_b))
    plt.bar(y_pos, times_b, align="center", alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Затраченное время, единицы времени")
    plt.title("Временная характеристика алгоритмов построения отрезков")

    plt.savefig(HIST_PATH)
    plt.clf()

    for i in range(TOTAL_DEGREES):
        steps[0].append(count_steps(points[i * 5]))
        steps[1].append(count_steps(points[i * 5 + 1]))
        steps[2].append(count_steps(points[i * 5 + 2]))
        steps[3].append(count_steps(points[i * 5 + 3]))
        steps[4].append(count_steps_wu(points[i * 5 + 4]))
    x = np.arange(TOTAL_DEGREES)
    # m = max(steps[4])
    # steps[4] = list(map(lambda x: abs(m - x), steps[4]))
    plt.ylabel("Количество ступенек")
    plt.xlabel("Угол")
    plt.plot(x, steps[0], color='r', label = 'DDA')
    plt.plot(x, steps[1], color='b', label = 'Bres. Int')
    plt.plot(x, steps[2], color='g', label = 'Bres. Float')
    plt.plot(x, steps[3], color='m', label = 'Bres. AA')
    plt.plot(x, steps[4], color='y', label = 'Wu')

    plt.title("Зависимость количества ступенек линии от угла")
    plt.legend()
    plt.savefig(PLOT_PATH)


def count_steps(points):
    n = 0
    x, y = points[0][0], points[0][1]
    for i in points:
        x_new, y_new = i[0], i[1]
        if x_new != x and y_new != y:
            n += 1
        x, y = x_new, y_new
    
    return n

def count_steps_wu(points):
    n = 0
    x, y = points[0][0], points[0][1]
    for i in range(len(points)//2):
        x_new, y_new = points[i*2][0], points[i*2][1]
        if x_new != x and y_new != y:
            n += 1
        x, y = x_new, y_new
    
    return n
