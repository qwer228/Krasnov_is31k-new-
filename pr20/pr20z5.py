class IntOnlyDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Разрешены только целые числа")
        self.value = value

class E: num = IntOnlyDescriptor()
e = E()
e.num = 5
# e.num = 5.5  # TypeError
