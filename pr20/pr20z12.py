class AgeDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)) or not (0 <= value <= 120):
            raise ValueError("Возраст должен быть от 0 до 120")
        self.value = value

class L: age = AgeDescriptor()
l = L()
l.age = 25
# l.age = 130  # ValueError
