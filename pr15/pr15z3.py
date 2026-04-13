import string

# Создаем тестовый файл
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, world! How are you?")

# Решение
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

clean_text = text.translate(str.maketrans('', '', string.punctuation))

with open('clean.txt', 'w', encoding='utf-8') as f:
    f.write(clean_text)

print("Текст сохранен в clean.txt")
