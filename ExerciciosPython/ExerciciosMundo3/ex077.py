palavras = ('AMOR', 'FE', 'GRATIDAO', 'LUZ', 'CAMINHO', 'CABOCLO', 'ARUANDA', 'ORACAO', 'TRABALHO'
            , 'VIDA', 'RAZAO', 'VIVER', 'ORIXA', 'DEUS', 'BENCAO')
for c in palavras:
    print(f'\nNa Palavra {c:^10} temos ', end='')
    for cont in c:
        if cont.lower() in 'aeiou':
            print(cont.lower(), end=' ')
