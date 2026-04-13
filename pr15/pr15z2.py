import re
from collections import Counter

# Создаем тестовый файл
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world! Hello python. Apple banana apple.")

# Решение
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)
    print("Слова и их количество по убыванию частоты:")
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")
