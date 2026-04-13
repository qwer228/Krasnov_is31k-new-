# Создаем тестовый файл
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("INFO All good\nERROR Database connection failed\nWARNING Low memory")

# Решение
with open('log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
