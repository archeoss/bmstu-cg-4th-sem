
from numpy import sign
def bresenhamInt(x1: float, y1: float, x2: float, y2: float):
    
    x1 = round(x1)
    y1 = round(y1)
    x2 = round(x2)
    y2 = round(y2)
    if x1 == x2 and y1 == y2:
        return [[x1, y1]]
    
    points = []

    deltaX = x2 - x1
    deltaY = y2 - y1

    stepX = int(sign(deltaX))
    stepY = int(sign(deltaY))

    deltaX = abs(deltaX)
    deltaY = abs(deltaY)

    if deltaX <= deltaY:
        deltaX, deltaY = deltaY, deltaX
        flag = True
    else:
        flag = False

    acc = deltaY + deltaY - deltaX
    cur_x = x1
    cur_y = y1

    for i in range(deltaX + 1):
        points.append([cur_x, cur_y])

        if acc >= 0:
            if flag:
                cur_x += stepX
            else:
                cur_y += stepY
            acc -= (deltaX + deltaX)
        if acc <= 0:
            if flag:
                cur_y += stepY
            else:
                cur_x += stepX
            acc += deltaY + deltaY

    return points
