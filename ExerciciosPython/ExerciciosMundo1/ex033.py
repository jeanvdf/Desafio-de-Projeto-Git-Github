print('Vamos Analisar 3 Números...')
n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo: '))
n3 = int(input('Digite o Terceiro: '))
#Minha Solução
'''if n1 > n2 > n3:
    print('O Maior Valor é o Primeiro: {}.'.format(n1))
else:
    if n2 > n3:
        print('O Maior Valor é o Segundo: {}.'.format(n2))
    else:
        print('O Maior Valor é o Terceiro: {}.'.format(n3))
if n1 < n2 < n3:
    print('O Menor Valor é o Primeiro: {}.'.format(n1))
else:
    if n2 < n3:
        print('O Menor Valor é o Segundo: {}.'.format(n2))
    else:
        print('O Menor Valor é o Terceiro: {}.'.format(n3))
# Solução do Professor
'''
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('O Maior Valor Digitado foi o {}'.format(maior))
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O Menor Valor Digitado Foi o {}'.format(menor))
