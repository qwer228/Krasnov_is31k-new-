class WithSlots:
    __slots__ = ('x',)
    def __init__(self, x): self.x = x

class WithoutSlots:
    def __init__(self, x): self.x = x

ws = WithSlots(10)
wo = WithoutSlots(10)

try:
    ws.y = 20  # ошибка
    print("WithSlots: атрибут добавлен")
except AttributeError:
    print("WithSlots: нельзя добавить новый атрибут")

wo.y = 20  #  Работает
print(f"WithoutSlots: y = {wo.y}")

