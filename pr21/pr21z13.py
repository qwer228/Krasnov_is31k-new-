class Person:
    __slots__ = ('name',)
    def __init__(self, name):
        self.name = name

class Student(Person):
    __slots__ = ('grade',)  # Важно: нужно объявить свои слоты
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

st = Student("Ольга", 5)
print(f"{st.name}, оценка: {st.grade}")
