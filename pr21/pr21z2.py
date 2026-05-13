class Animal:
    __slots__ = ('type', 'weight')
    
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

a = Animal("Собака", 15.5)
try:
    a.color = "brown"  # Вызовет AttributeError
except AttributeError as e:
    print(f"Ошибка: {e}")
# Объяснение: __slots__ запрещает создание атрибутов, не указанных в кортеже
