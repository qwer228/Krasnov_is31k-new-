# Создаем тестовый файл
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Short line\nThis is a much longer line\nAnother line")

# Решение
with open('input.txt', 'r', encoding='utf-8') as f:
    longest_line = max(f, key=len).strip("\n")
    print(f"Длина: {len(longest_line)}")
    print(f"Строка: {longest_line}")
