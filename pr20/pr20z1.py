class SimpleDescriptor:
    def __init__(self, default=None):
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        self.value = value

class A: attr = SimpleDescriptor(10)
a = A()
print(a.attr)  # 10
a.attr = 42
print(a.attr)  # 42
