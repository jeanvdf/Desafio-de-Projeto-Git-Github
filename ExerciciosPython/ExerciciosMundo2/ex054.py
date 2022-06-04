print('Vamos Ler O ANO De Nascimento de 7 Pessoas..')
maior = 0
menor = 0
from datetime import date
anoatual = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o Ano de Nascimento da {}ª pessoa: '.format(c)))
    print('{} anos.'.format(anoatual - ano))
    if anoatual - ano >= 21:
        maior += 1
    else:
        menor += 1
print(' {} Pessoas São Maiores de Idade.'.format(maior))
print(' {} Pessoas São Menores de Idade.'.format(menor))