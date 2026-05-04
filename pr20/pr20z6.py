class PositiveDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Число должно быть > 0")
        self.value = value

class F: pos = PositiveDescriptor()
f = F()
f.pos = 3.14
# f.pos = -1  # ValueError
