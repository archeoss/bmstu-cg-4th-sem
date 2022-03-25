def dda(x1 : float, y1 : float, x2 : float, y2 : float):
    # if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
    #     raise TypeError
    points = []
    dx, dy = x2 - x1, y2 - y1
    x, y = round(x1), round(y1)

    steps = (max(abs(dx), abs(dy)))
    x_incr, y_incr = dx / steps, dy / steps
    steps = round(steps)
    for i in range(steps + 1):
        points.append([(round(x)), (round(y)), 255])
        x += x_incr
        y += y_incr
    
    return points