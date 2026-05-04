class CounterDescriptor:
    def __init__(self, default=None):
        self.value = default
        self.get_count = 0
    def __get__(self, obj, objtype=None):
        self.get_count += 1
        return self.value
    def __set__(self, obj, value):
        self.value = value

class I: tracked = CounterDescriptor(0)
i = I()
i.tracked; i.tracked; i.tracked
print(i.tracked.get_count)  # 3
