with open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    if not content.strip():
        print("Empty")
    else:
        print("Файл не пустой")
