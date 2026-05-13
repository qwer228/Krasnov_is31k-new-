class Product:
    __slots__ = ('name', 'price')
    
    def __init__(self, name, price):
        self.name = name
        if price < 0:
            raise ValueError(" Цена не может быть отрицательной!")
        self.price = price

try:
    p = Product("Товар", -100)
except ValueError as e:
    print(e)

p = Product("Товар", 299.99)
print(f"{p.name}: {p.price} ₽")

