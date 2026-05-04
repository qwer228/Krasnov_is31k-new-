class DefaultDescriptor:
    def __init__(self):
        self._value = None
        self._is_set = False
    def __get__(self, obj, objtype=None):
        return self._value if self._is_set else 'default'
    def __set__(self, obj, value):
        self._value = value
        self._is_set = True

class H: opt = DefaultDescriptor()
h = H()
print(h.opt)  # default
h.opt = "custom"
print(h.opt)  # custom
