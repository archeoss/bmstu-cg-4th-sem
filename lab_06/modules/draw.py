from PyQt6.QtGui import QPixmap, QPainter, QColor
from PyQt6.QtCore import QCoreApplication, QEventLoop
from .graphicsView import GraphicsView


def fill_polygon(view: GraphicsView, color: list[3],  border_color: list[3],
                 isDelay: bool = False, delayTime: int = 1):
    scene = view.scene()
    paintDevice = QPixmap(int(scene.sceneRect().width()), int(scene.sceneRect().height()))
    painter = QPainter()
    painter.begin(paintDevice)
    scene.render(painter)
    pixels = paintDevice.toImage()
    stack = view.prefilledPoints.copy()
    colors = [(*color, 255), (*border_color, 255)]
    delayTime = delayTime // 2 + 1
    painter.setPen(QColor(*color))
    cur_d = delayTime

    while stack:
        point = stack.pop()
        painter.drawPoint(point[0], point[1])

        x, y = point[0] + 1, point[1]
        pixel = pixels.pixelColor(x, y).getRgb()
        while pixel not in colors:
            painter.drawPoint(x, y)
            x += 1
            pixel = pixels.pixelColor(x, y).getRgb()
        rborder = x - 1

        x = point[0] - 1
        pixel = pixels.pixelColor(x, y).getRgb()
        while pixel not in colors:
            painter.drawPoint(x, y)
            x -= 1
            pixel = pixels.pixelColor(x, y).getRgb()
        lborder = x + 1

        sign = [1, -1]

        for i in sign:
            x = lborder
            y = point[1] + i

            while x <= rborder:
                is_exist = False
                pixel = pixels.pixelColor(x, y).getRgb()
                while pixel not in colors and x <= rborder:
                    is_exist = True
                    x += 1
                    pixel = pixels.pixelColor(x, y).getRgb()
                if is_exist:
                    stack.extend([[x - 1, y]])
                    is_exist = False
                xi = x
                pixel = pixels.pixelColor(x, y).getRgb()
                while pixel not in colors and x <= rborder:
                    x += 1
                    pixel = pixels.pixelColor(x, y).getRgb()
                if x == xi:
                    x += 1
        cur_d -= 1
        if isDelay and cur_d == 0:
            cur_d = delayTime
            make_delay(scene, paintDevice)
        pixels = paintDevice.toImage()
    scene.addPixmap(paintDevice)
    scene.render(painter)
    view.setScene(scene)
    view.update()
    painter.end()


def make_delay(scene, paintDevice):
    
    QCoreApplication.processEvents(QEventLoop.ProcessEventsFlag.AllEvents, 0)
    scene.addPixmap(paintDevice)
