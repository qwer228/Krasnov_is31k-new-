class CachedDescriptor:
    def __init__(self, compute_func):
        self.func = compute_func
        self.cache = {}
    def __get__(self, obj, objtype=None):
        if obj is None: return self
        if obj not in self.cache:
            print("Вычисление...")
            self.cache[obj] = self.func(obj)
        return self.cache[obj]

class Q:
    heavy = CachedDescriptor(lambda self: sum(range(100000)))
q = Q()
print(q.heavy)  # Вычисление... 4999950000
print(q.heavy)  # (без вычисления, берётся из кэша) 4999950000
