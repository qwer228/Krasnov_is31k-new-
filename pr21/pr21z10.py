class Employee:
    __slots__ = ('name', 'salary')
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def raise_salary(self, percent):
        self.salary *= (1 + percent / 100)
        print(f" Новая зарплата {self.name}: {self.salary:.2f}")

emp = Employee("Мария", 50000)
emp.raise_salary(10)

