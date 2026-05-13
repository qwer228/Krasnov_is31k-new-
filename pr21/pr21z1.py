class Person:
    __slots__ = ('name', 'age')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Анна", 25)
print(f"Имя: {p.name}, Возраст: {p.age}")
