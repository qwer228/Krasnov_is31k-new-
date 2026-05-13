class Temperature:
    __slots__ = ('value',)
    
    def __init__(self, value):
        self.value = value  # в Цельсиях
    	
    def to_fahrenheit(self):
        return self.value * 9/5 + 32

t = Temperature(25)
print(f"{t.value}°C = {t.to_fahrenheit()}°F")
