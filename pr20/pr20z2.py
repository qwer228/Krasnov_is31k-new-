class LogGetDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        print("Getting value")
        return self.value
    def __set__(self, obj, value):
        self.value = value

class B: val = LogGetDescriptor(5)
b = B()
b.val  # Вывод: Getting value \n 5
