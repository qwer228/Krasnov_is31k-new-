class InstanceCounterDescriptor:
    _counter = 0
    def __get__(self, obj, objtype=None):
        return InstanceCounterDescriptor._counter
    def __set__(self, obj, value):
        InstanceCounterDescriptor._counter = value

class S:
    count = InstanceCounterDescriptor()
    def __init__(self):
        # Увеличиваем счётчик при создании
        S.count += 1

s1 = S()
s2 = S()
print(s1.count, s2.count)  # 2 2
