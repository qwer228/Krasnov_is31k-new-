class NumberListDescriptor:
    def __init__(self, default=None):
        self.value = default if default is not None else []
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, (list, tuple)):
            raise TypeError("Ожидается список или кортеж")
        if not all(isinstance(x, (int, float)) for x in value):
            raise ValueError("Все элементы должны быть числами")
        self.value = list(value)

class R: nums = NumberListDescriptor()
r = R()
r.nums = [1, 2.5, 3]
# r.nums = [1, "a", 3]  # ValueError
