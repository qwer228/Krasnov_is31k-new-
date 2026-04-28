import os
if os.path.exists("data.txt"):
    print(os.path.getsize("data.txt"))  # размер в байтах
else:
    print("Файл не найден.")
