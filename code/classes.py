class Point:
    """This is a point representation"""

    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    """This is a line representation"""

    def __init__(self, x1, y1, x2, y2) -> None:
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
