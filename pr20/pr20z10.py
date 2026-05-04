class ShortStringDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Ожидается строка")
        if len(value) > 10:
            raise ValueError("Максимум 10 символов")
        self.value = value

class J: short = ShortStringDescriptor()
j = J()
j.short = "ok"
# j.short = "слишком длинная строка"  # ValueError
