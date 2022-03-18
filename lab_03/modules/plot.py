from .algorithms.bresenham import *
from .algorithms.dda import *
from .algorithms.wu import *
from .draw import *
import time
import matplotlib.pyplot as plt
import numpy as np

TIMES = 10

def makeGisto():
    step = 1
    rad = 250
    angle = 0
    center_x = center_y = 0
    timer = [[], [], [], [], [], []]
    points = []
    steps = [[], [], [], [], []]
    while (angle < MAX_ANGLE):
        x = sin(radians(angle)) * rad
        y = cos(radians(angle)) * rad
        times = []
        for i in range(TIMES):
            start = time.time()
            p = dda(round(center_x), round(center_y), round(x), round(y))
            end = time.time()
            times.append(end - start)
        timer[0].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = breisenhamInt(round(center_x), round(center_y), round(x), round(y))
            end = time.time()
            times.append(end - start)
        timer[1].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = breisenhamFloat(round(center_x), round(center_y), round(x), round(y))
            end = time.time()
            times.append(end - start)
        timer[2].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = breisenhamAA(round(center_x), round(center_y), round(x), round(y))
            end = time.time()
            times.append(end - start)
        timer[3].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        points.append(list(p))

        times = []
        for i in range(TIMES):
            start = time.time()
            p = Wu(round(center_y), round(center_x), round(y), round(x))
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
            painter.drawLine(QPoint(round(center_x), round(center_y)), QPoint(round(x), round(y)))
            end = time.time()
            painter.end()
            times.append(end - start)
        timer[5].append((sum(times) - min(times) - max(times)) / (TIMES - 2))
        
        angle += step
    times_b = list(map(lambda x: sum(x)/len(x), timer))
    objects = ['DDA', 'Bres. Int', 'Bres. Float', 'Bres. AA', 'Wu','Lib.Line']
    y_pos = np.arange(len(times_b))
    plt.bar(y_pos, times_b, align="center", alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Затраченное время, единицы времени")
    plt.title("Временная характеристика алгоритмов построения отрезков")

    for i in range(360):
        steps[0].append(count_steps(points[i * 5]))
        steps[1].append(count_steps(points[i * 5 + 1]))
        steps[2].append(count_steps(points[i * 5 + 2]))
        steps[3].append(count_steps(points[i * 5 + 3]))
        steps[4].append(count_steps(points[i * 5 + 4]))
    x = np.arange(360)
    
    plt.plot(x, steps[0], color='r', label = 'DDA')
    plt.plot(x, steps[1], color='b', label = 'Bres. Int')
    plt.plot(x, steps[2], color='g', label = 'Bres. Float')
    plt.plot(x, steps[3], color='m', label = 'Bres. AA')
    plt.plot(x, steps[4], color='y', label = 'Wu')

    plt.legend()
    plt.show()

def count_steps(points):
    n = 0
    x, y = points[0][0], points[0][1]
    for i in points:
        x_new, y_new = i[0], i[1]
        if x_new != x and y_new != y:
            n += 1
        x, y = x_new, y_new
    
    return n
