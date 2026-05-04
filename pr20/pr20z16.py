class LinkedDescriptor:
    def __init__(self, link_attr, default=None):
        self.link_attr = link_attr
        self.value = default
    def __get__(self, obj, objtype=None):
        return self.value
    def __set__(self, obj, value):
        self.value = value
        # Автоматически обновляем связанное поле
        setattr(obj, self.link_attr, value)

class P:
    width = LinkedDescriptor("height")
    height = None
p = P()
p.width = 10
print(p.height)  # 10
