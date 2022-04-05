from modules.basic_func import append_points_circ, append_points_el

def brescircle(x_center : float, y_center : float, radius : float, color : list[int, 3]):
    points = []
    x = 0
    y = int(radius)
    x_center, y_center = int(x_center), int(y_center)
    
    delta = 2 * (1 - radius)

    append_points_circ(points, x + x_center, y + y_center, x_center, y_center, color)

    while x < y:
        if delta <= 0:
            delta_temp = 2 * (delta + y) - 1
            x += 1
            if delta_temp >= 0:
                y -= 1
                delta += 2 * (x - y + 1)
            else:
                delta += 2 * x + 1

        else:
            delta_temp = 2 * (delta - x) - 1
            y -= 1
            if delta_temp < 0:
                x += 1
                delta += 2 * (x - y + 1)
            else:
                delta -= 2 * y - 1

        append_points_circ(points, x + x_center, y + y_center, x_center, y_center, color)

    return points

def bresellipse(x_center, y_center, frad, srad, color):
    x_center, y_center, frad, srad = round(x_center), round(y_center), round(frad), round(srad)
    
    points = []
    x = 0
    y = round(srad)

    a, b = round(frad ** 2), round(srad ** 2)
    delta = b - a * (2 * srad - 1)

    #append_points_el(points, x + x_center, y + y_center, x_center, y_center, color)

    while y >= 0:
        append_points_el(points, x + x_center, y + y_center, x_center, y_center, color)

        if delta < 0:
            delta_temp = 2 * delta + a * (2 * y - 1)
            x += 1
            delta += b * (2 * x + 1)
            if delta_temp >= 0:
                y -= 1
                delta += a * (-2 * y + 1)
        elif delta == 0:
            x += 1
            y -= 1
            delta += b * (2 * x + 1) + a * (-2 * y + 1)
        else:
            delta_temp = 2 * delta + b * (-2 * x - 1)
            y -= 1
            delta += a * (-2 * y + 1)
            if delta_temp <= 0:
                x += 1
                delta += b * (2 * x + 1)

        
    return points