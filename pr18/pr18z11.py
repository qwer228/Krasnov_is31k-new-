with open('input.txt', 'r', encoding='utf-8') as src, \
     open('output.txt', 'w', encoding='utf-8') as dst:
    dst.writelines(src.readlines())
