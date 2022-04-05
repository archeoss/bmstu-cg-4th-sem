from modules.basic_func import *

def midpcircle(x_center, y_center, radius, color):

    points = []
    x = int(radius)
    y = 0
    x_center, y_center = int(x_center), int(y_center)
    append_points_circ(points, x + x_center, y + y_center, x_center, y_center, color)
    delta = 1 - radius

    while x > y:
        y += 1
        if delta >= 0:
            x -= 1
            delta += 2 * (y - x) + 1# - 2
        else:
            delta += 2 * y  + 1#+ 2
        append_points_circ(points, x + x_center, y + y_center, x_center, y_center, color)

    return points


def midpellipse(x_center, y_center, frad, srad, color):
    points = []
    x = 0
    y = int(srad)
    x_center, y_center = int(x_center), int(y_center)
    a, b = srad ** 2,  frad ** 2
    delta = a - b * srad + 0.25 * b
    dx = 2 * a * x
    dy = 2 * b * y

    while dx < dy:
        append_points_el(points, x + x_center, y + y_center, x_center, y_center, color)

        x += 1
        dx += 2 * a

        if delta > 0:
            y -= 1
            dy -= 2 * b
            delta -= dy

        delta += dx + a

    delta = a * (x + 0.5)**2 + b * (y - 1)**2 - b * a

    while y >= 0:
        append_points_el(points, x + x_center, y + y_center, x_center, y_center, color)

        y -= 1
        dy -= 2 * b

        if delta <= 0:
            x += 1
            dx += 2 * a
            delta += dx

        delta -= dy - b

    return points
