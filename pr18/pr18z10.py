with open('input.txt', 'r', encoding='utf-8') as src, \
     open('output_upper.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        dst.write(line.upper())
