s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print('A Soma Entre os Números Ímpares e Divisiveis Por 3, entre 1 e 500,  é {} .'.format(s))
