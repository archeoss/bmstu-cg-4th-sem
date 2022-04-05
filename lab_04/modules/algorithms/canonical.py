from modules.basic_func import *
from math import sqrt, pow

def canonical_circle(x_center, y_center, radius, alpha):
    """
        Implementation of circle canonical equation method.
    """
    x_center, y_center, radius = round(x_center), round(y_center), round(radius)
    points = []
    R = radius ** 2
    for x in range(x_center, round(x_center + (radius / sqrt(2)) + 1)):
        y = round(sqrt(R - pow(x - x_center, 2)) + y_center)
        append_points_circ(points, x, y, x_center, y_center, alpha)

    return points


def canonical_ellipse(x_center, y_center, frad, srad, alpha):
    """
        Implementation of ellipse canonical equation method.
    """
    x_center, y_center, frad, srad = round(x_center), round(y_center), round(frad), round(srad)
    points = []
    a, b = srad ** 2, frad ** 2
    const = b * a
    limit = round(x_center + frad / sqrt(1 + a / b))
    
    for x in range(x_center, limit + 1):
        y = round(sqrt(const - pow(x - x_center, 2) * a) / frad + y_center)
        append_points_el(points, x, y, x_center, y_center, alpha)

    limit = round(y_center + srad / sqrt(1 + b / a))

    for y in range(limit, y_center - 1, -1):
        x = round(sqrt(const - pow(y - y_center, 2) * b) / srad + x_center)
        append_points_el(points, x, y, x_center, y_center, alpha)

    return points