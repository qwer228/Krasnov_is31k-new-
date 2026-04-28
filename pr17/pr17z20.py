import random
import datetime
import os

# 1. Генерация 5 случайных чисел
numbers = [random.randint(1, 100) for _ in range(5)]
current_date = datetime.date.today()

# 2,3. Запись в файл с датой
filename = "numbers.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Дата записи: {current_date}\n")
    f.write("Случайные числа: " + ", ".join(map(str, numbers)) + "\n")

# 4. Проверка существования файла
if os.path.exists(filename):
    print(f" Файл '{filename}' существует.")
    # 5. Чтение и вывод содержимого
    with open(filename, "r", encoding="utf-8") as f:
        print("Содержимое файла:")
        print(f.read())
else:
    print(f" Файл '{filename}' не найден.")
