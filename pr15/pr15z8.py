# Создаем тестовый файл
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("apple\nBanana\ncherry\nDog")

# Решение
count = 0
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.strip() and line[0].isupper():
            count += 1

print(f"Строк с заглавной буквы: {count}")
