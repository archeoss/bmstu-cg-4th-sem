from .graphicsView import GraphicsView

def get_code(x, y, rect):
    # rect = [Х левый, Х правый, У нижнее, У верхнее]
    code = [0, 0, 0, 0]
    if x < rect[0]: # X < X левый
        code[0] = 1
    if x > rect[1]: # X > X правый
        code[1] = 1
    if y > rect[2]: # У > У нижнее
        code[2] = 1
    if y < rect[3]: # У < У верхнее
        code[3] = 1

    return code

# Отсечение!!!
# Отсечение производится в определенном порядке:
# левой, правой, нижней, верхней границами отсекателя.
def clipping(view : GraphicsView):
    for b in view.lines:
        cohen_sutherland(view, b, view.cutter) 
   


def log_prod(code1, code2):
    p = 0
    for i in range(4):
        p += code1[i] & code2[i]

    return p

#  Видимость
def is_visible(x1, y1, x2, y2, rect):
    """Видимость - 0 = невидимый
                   1 = видимый
                   2 = частично видимый"""
    # вычисление кодов концевых точек отрезка
    s1 = sum(get_code(x1, y1, rect))
    s2 = sum(get_code(x2, y2, rect))

    # предположим, что отрезок частично видим
    vis = 2

    # проверка полной видимости отрезка
    if not s1 and not s2:
        vis = 1
    else:
        # проверка тривиальной невидимости отрезка
        l = log_prod(get_code(x1, y1, rect), get_code(x2, y2, rect))
        if l != 0:
            vis = 0

    return vis


def cohen_sutherland(view : GraphicsView, bar, rect):
    
    # инициализация флага
    flag = 0 # общего положения
    m = 1

    # проверка вертикальности и горизонтальности отрезка
    x1,y1,x2,y2 = bar[0], bar[1], bar[2], bar[3]
    if x2 - x1 == 0:
        flag = -1   # вертикальный отрезок
    else:
        # вычисление наклона
        m = (y2 - y1) / (x2 - x1)
        if m == 0:
            flag = 1   # горизонтальный

    # для каждой стороны окна
    # Когда у нас вертикаль - то пропускается i = 0 и i = 1 
    # Когда у нас горизонталь - то пропускаем i = 2 и i = 3
    for i in range(4):
        """Видимость - 0 = невидимый
                       1 = видимый
                       2 = частично видимый"""
        # Опредление видимости
        vis = is_visible(x1, y1, x2, y2, rect)
        # Если тривиально видим (полностью видим), то рисуем и выходим из цикла
        if vis == 1:
            pixmap = view.drawLine(view.linesPixmap, x1, y1, x2, y2, view.resultColor)
            view.update(view.backgroundPixmap, pixmap, view.cutterPixmap)
            return
        # Иначе проверяем на невидимость (тривиальную невидимость), 
        # то выход из цикла
        elif not vis:
            return

        # проверка пересечения отрезка и стороны окна
        code1 = get_code(x1, y1, rect)
        code2 = get_code(x2, y2, rect)

        # Если Т1 == Т2, то переход на след шаг цикла
        if code1[i] == code2[i]:
            continue

        
        # проверка нахождения Р1 вне окна; если Р1 внутри окна, 
        # то Р2 и Р1 поменять местами
        # Если Т1 == 0, то обмен местами точек, 
        # (так как мы всегда принимаем Р1 за невидимую)
        if not code1[i]:
            x1, y1, x2, y2 = x2, y2, x1, y1


        # поиск пересечений отрезка со сторонами окна
        # Проверка  вертикальности  отрезка:  если Fl =-1, то переход к y1 = rect[i]
        if flag != -1:
            if i < 2:
                y1 = m * (rect[i] - x1) + y1
                x1 = rect[i]
                continue
            else:
                x1 = (1 / m) * (rect[i] - y1) + x1
        y1 = rect[i]
    pixmap = view.drawLine(view.linesPixmap, x1, y1, x2, y2, view.resultColor)
    view.update(view.backgroundPixmap, pixmap, view.cutterPixmap)

