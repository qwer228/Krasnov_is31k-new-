import re

# Создаем тестовый файл
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world! Hello Python.")

# Решение
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    unique_words = set(words)
    print(f"Количество уникальных слов: {len(unique_words)}")
