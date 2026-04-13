# Создаем тестовый файл
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Line 1\nLine 2\nLine 1\nLine 3\n")

# Решение
seen = set()
with open('input.txt', 'r', encoding='utf-8') as infile, \
        open('unique.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        if line not in seen:
            outfile.write(line)
            seen.add(line)

print("Уникальные строки сохранены в unique.txt")
