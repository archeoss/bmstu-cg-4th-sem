def append_points_circ(points : list, x : int, y : int, x_center : int, y_center : int, alpha : int):
    
    points.extend([
        [x, y, alpha],
        [2 * x_center - x, y, alpha],
        [x, 2 * y_center - y, alpha],
        [2 * x_center - x, 2 * y_center - y, alpha],
        [y + x_center - y_center, x + y_center - x_center, alpha],
        [-y + x_center + y_center, x + y_center - x_center, alpha],
        [y + x_center - y_center, -x + y_center + x_center, alpha],
        [-y + x_center + y_center, -x + y_center + x_center, alpha]
    ])

def append_points_el(points : list, x : int, y : int, x_center : int, y_center : int, alpha : int):
    
    points.extend([
        [x, y, alpha],
        [2 * x_center - x, y, alpha],
        [x, 2 * y_center - y, alpha],
        [2 * x_center - x, 2 * y_center - y, alpha],
    ])

