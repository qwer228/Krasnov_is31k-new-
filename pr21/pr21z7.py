class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def coords(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(f"Координаты: {p.coords()}")
