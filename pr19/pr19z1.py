import time

def task1():
    for i in range(3):
        print(f"Task1: {i}")
        time.sleep(0.5)

def task2():
    for i in range(3):
        print(f"Task2: {i}")
        time.sleep(0.5)

# Последовательное выполнение
print(" Последовательно ")
task1()
task2()

# Псевдопараллельное 
print("\n Псевдопараллельно ")
for _ in range(3):
    task1.__code__ = task1.__code__  # просто демонстрация концепции
    # В реальности используется asyncio или threading









for _ in range(3):
    task1.__code__ = task1.__code__  # просто демонстрация концепции
    # В реальности используется asyncio или threading
