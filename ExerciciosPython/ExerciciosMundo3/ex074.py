from random import randint
lista = (randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30))
print('Os Valores Sorteados Foram: ', end=' ')
for c in lista:
    print(c, end=' ')
print(f'\nO Maior valor é {max(lista)}, e o menor valor é {min(lista)}.')
