class RoundDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Ожидается число")
        self.value = round(value, 2)

class M: price = RoundDescriptor()
m = M()
m.price = 10.5678
print(m.price)  # 10.57
