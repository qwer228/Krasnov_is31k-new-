# Создаем тестовые файлы
with open('file1.txt', 'w', encoding='utf-8') as f: f.write("Data from file 1\n")
with open('file2.txt', 'w', encoding='utf-8') as f: f.write("Data from file 2\n")

# Решение
files_to_merge = ['file1.txt', 'file2.txt']

with open('result.txt', 'w', encoding='utf-8') as outfile:
    for fname in files_to_merge:
        with open(fname, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())

print("Файлы объединены в result.txt")
