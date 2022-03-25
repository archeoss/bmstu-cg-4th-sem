def breisenhamFloat(x1 : float, y1 : float, x2 : float, y2 : float):
    # if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
    #     raise TypeError
    points = []

    dx, dy = x2 - x1, y2 - y1
    x_sign = 1 if dx > 0 else -1
    y_sign = 1 if dy > 0 else -1
    dx, dy = abs(dx), abs(dy)
    
    turned = False
    x, y = round(x1), round(y1)
    if dx < dy:
        turned = True
        x, y = y, x
        dx, dy = dy, dx
        x_sign, y_sign = y_sign, x_sign

    d_err = dy / dx 
    err = d_err - 0.5
    for i in range(round(dx) + 1):
        points.append([y, x, 255] if turned else [x, y, 255])
        
        if err >= 0:
            y += y_sign
            err -= 1
        if err <= 0:
            err += d_err
            x += x_sign
        
    return points

def breisenhamInt(x1 : float, y1 : float, x2 : float, y2 : float):
    # if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
    #     raise TypeError
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
        if f < 0:
            f += incr_b
            x += x_sign

    return points

def breisenhamAA(x1 : float, y1 : float, x2 : float, y2 : float):
    # if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
    #     raise TypeError
    points = []

    I = 255
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

    tg = I * dy / dx
    err = 0.5 * I
    w = I - tg
    for i in range(round(dx) + 1):
        points.append([y, x, int(err)] if turned else [x, y, int(err)])

        if err < w:
            err += tg
            x += x_sign
        else:
            y += y_sign
            x += x_sign
            err -= w
        
    return points

