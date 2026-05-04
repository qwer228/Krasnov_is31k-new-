class StringDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Ожидается строка")
        self.value = value

class G: name = StringDescriptor()
g = G()
g.name = "Alice"
# g.name = 123  # TypeError
