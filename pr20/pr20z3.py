class LogSetDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        print("Setting value")
        self.value = value

class C: val = LogSetDescriptor()
c = C()
c.val = 99  # Вывод: Setting value
