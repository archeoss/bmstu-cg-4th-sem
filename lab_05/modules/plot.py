from .draw import *
import time
import matplotlib.pyplot as plt
import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6 import QtCore
from math import sin, cos, radians
NUM_OF_POINTS = 6
RADUIS = 50
TIMES = 7
COUNT = 30
STEP = 5
MIN_INDEX = 1
MAX_INDEX = 4
PLOT_PATH = os.path.join(os.path.dirname(__file__), 'plots/plot.png')
FIGURE_PATH = os.path.join(os.path.dirname(__file__), 'plots/figure.png')

def makePlot():
    rad = RADUIS
    timer = []
    rads = []
    for j in range(COUNT):

        view = GraphicsView()
        view.setGeometry(QtCore.QRect(0, 0, 1011, 731))
        view.fillColor = [255, 255, 255]
        view.bordColor = [255, 0, 0]
        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, view.width() - 10, view.height() - 10)

        pixmap = QPixmap(int(scene.width()), int(scene.height()))
        pixmap.fill(QColor('black'))
        scene.addPixmap(pixmap)

        view.setScene(scene)
        angle = 0
        step = 360 / NUM_OF_POINTS
        for i in range(NUM_OF_POINTS + 1):
            x = round(sin(radians(angle)) * rad) + 400
            y = round(cos(radians(angle)) * rad) + 400
            if view.isNew:
                view.isNew = False
                view.points.append([])
                view.start_point = [x, y]
            view.points[-1].append([x, y])
            view.draw()
            angle += step
        
        times = []
        for i in range(TIMES):
            start = time.time()
            fill_polygon(view, [255,255,255], [0,0,0], [255, 0, 0])
            end = time.time()
            times.append(end - start)
            
        times.sort()
        timer.append((sum(times[MIN_INDEX:MAX_INDEX + 1])) / (MAX_INDEX - MIN_INDEX))
        rads.append(rad)
        rad += STEP
        
        # if j == 0:
        #     scene = view.scene()        
        #     paintDevice = QPixmap(int(scene.sceneRect().width()), int(scene.sceneRect().height()))
        #     painter = QPainter()
        #     painter.begin(paintDevice)
        #     scene.render(painter)
        #     paintDevice.toImage().save(FIGURE_PATH)
        #     painter.end()

    plt.ylabel("Время")
    plt.xlabel("Радиус круга")
    plt.plot(rads, timer, color='r', label = 'Canonic')
    # plt.plot(rad, time_circle[4], color='y', label = 'Lib (PyQt6)')

    plt.title("Зависимость времени построения круга от радиуса")
    plt.legend()
    plt.savefig(PLOT_PATH)
    plt.clf()

