with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    word_count = len(content.split())
    print(f"Количество слов: {word_count}")
