class Order:
    __slots__ = ('items',)
    
    def __init__(self, items):
        self.items = items  # список цен
    
    def total(self):
        return sum(self.items)

order = Order([100, 250, 75.5])
print(f"Общая стоимость: {order.total()} ₽")
