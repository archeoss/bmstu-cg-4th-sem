def fpart(x):
    return x - int(x)
 
def rfpart(x):
    return 1 - fpart(x)

def Wu(x1 : float, y1 : float, x2 : float, y2 : float):
    # if not isinstance(x1, float) or not isinstance(y1, float) or not isinstance(x2, float) or not isinstance(y2, float):
    #     raise TypeError
    points = []
    I = 255
    dx = x2 - x1
    dy = y2 - y1

    steep = abs(dx) < abs(dy)

    def p(px, py):
        return ([px, py], [py, px])[steep]

    if steep:
        x1, y1, x2, y2, dx, dy = y1, x1, y2, x2, dy, dx
    if x2 < x1:
        x1, x2, y1, y2 = x2, x1, y2, y1

    m = dy / dx
    intery = y1 + rfpart(x1) * m

    def get_endpoint(x_s, y_s):
        x_e = round(x_s)
        y_e = y_s + (x_e - x_s) * m
        x_gap = rfpart(x_s + 0.5)

        px, py = int(x_e), int(y_e)

        dens1 = rfpart(y_e) * x_gap
        dens2 = fpart(y_e) * x_gap

        points.append([*p(px, py), int(I * dens1)])
        points.append([*p(px, py), int(I * dens2)])

        return px

    x_s = get_endpoint(x1, y1) + 1
    x_e = get_endpoint(x2, y2)

    for x in range(x_s, x_e):
        y = int(intery)

        dens2 = intery - int(intery)
        dens1 = 1 - dens2
        points.append([*p(x, y), int(I * dens1)])
        points.append([*p(x, y+1), int(I * dens2)])

        intery += m

    return points
