def bresenhamInt(x1: float, y1: float, x2: float, y2: float):
    if x1 == x2 and y1 == y2:
        return [[x1, y1]]
    points = []

    dx, dy = x2 - x1, y2 - y1
    x_sign = 1 if dx > 0 else -1
    y_sign = 1 if dy > 0 else -1
    dx, dy = abs(dx), abs(dy)
    
    x, y = round(x1), round(y1)
    
    turned = False
    if dx < dy:
        turned = True
        x, y = y, x
        dx, dy = dy, dx
        x_sign, y_sign = y_sign, x_sign

    incr_a = -2 * dx
    incr_b = 2 * dy
    f = incr_b - dx
    for i in range(round(dx) + 1):
        points.append([y, x, 255] if turned else [x, y, 255])
        if f > 0:
            f += incr_a
            y += y_sign
        if f <= 0:
            f += incr_b
            x += x_sign

    return points