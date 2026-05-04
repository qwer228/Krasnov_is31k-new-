class OnceDescriptor:
    def __init__(self, default=None):
        self.value = default
        self.is_locked = False
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        if self.is_locked:
            raise AttributeError("Значение уже задано и не может быть изменено")
        self.value = value
        self.is_locked = True

class N: readonly = OnceDescriptor("init")
n = N()
n.readonly = "first"
# n.readonly = "second"  # AttributeError
