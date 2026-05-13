class Student:
    __slots__ = ('name', 'grade')
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def set_grade(self, new_grade):
        self.grade = new_grade
        print(f" Оценка {self.name} изменена на {new_grade}")

s = Student("Иван", 4)
s.set_grade(5)
