class EmailDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Некорректный email")
        self.value = value

class K: email = EmailDescriptor()
k = K()
k.email = "test@mail.ru"
# k.email = "invalid"  # ValueError
