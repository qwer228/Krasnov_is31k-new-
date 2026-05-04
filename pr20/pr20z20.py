class ComplexDescriptor:
    def __init__(self, expected_type, min_val=None, max_val=None, default=None):
        self.type = expected_type
        self.min = min_val
        self.max = max_val
        self.value = default
    def __get__(self, obj, objtype=None):
        print(f"[LOG] Get: {self.value}")
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, self.type):
            raise TypeError(f"Тип должен быть {self.type.__name__}")
        if self.min is not None and value < self.min:
            raise ValueError(f"Минимум: {self.min}")
        if self.max is not None and value > self.max:
            raise ValueError(f"Максимум: {self.max}")
        print(f"[LOG] Set: {value}")
        self.value = value
    def __delete__(self, obj):
        raise AttributeError("Удаление атрибута запрещено")

class T: score = ComplexDescriptor(int, 0, 100, 50)
t = T()
t.score  # [LOG] Get: 50
t.score = 75  # [LOG] Set: 75
# del t.score  # AttributeError
