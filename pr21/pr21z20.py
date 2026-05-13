class Student:
    __slots__ = ('name', 'age', 'grades')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, value):
        if 2 <= value <= 5:
            self.grades.append(value)
        else:
            print(" Оценка должна быть от 2 до 5")
    
    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Создаём студентов
s1 = Student("Анна", 20)
s1.add_grade(5); s1.add_grade(4); s1.add_grade(5)

s2 = Student("Дмитрий", 22)
s2.add_grade(3); s2.add_grade(4)

print(f"{s1.name}: средний балл = {s1.average():.2f}")
print(f"{s2.name}: средний балл = {s2.average():.2f}")

# Проверка: нельзя добавить новый атрибут
try:
    s1.course = "Python"
except AttributeError:
    print(" __slots__ работает: нельзя добавить атрибут 'course'")
