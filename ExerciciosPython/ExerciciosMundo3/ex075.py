lista = (int(input('Digite um Número: ')),
         int(input('Digite outro Número: ')),
         int(input('Digite mais um Número: ')),
         int(input('Digite o último Número: ')))
print(f'Você Digitou os Valores {lista}.')
print(f'O Valor 9 Aparece {lista.count(9)} vezes.')
if 3 in lista:
    print(f'o Valor 3 Aparece na {lista.index(3) + 1}ª posição.')
else:
    print('O Valor 3 Não aparece em nenhuma posição. ')
if lista[0] % 2 == 0 or lista[1] % 2 == 0 or lista[2] % 2 == 0 or lista[3] % 2 == 0:
    print('Os Valores Pares São: ', end='')
else:
    print('Não Há Valores Pares.')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
