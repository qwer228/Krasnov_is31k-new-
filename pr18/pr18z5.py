with open('input.txt', 'r', encoding='utf-8') as file:
    line_count = sum(1 for _ in file)
    print(f"Количество строк: {line_count}")
