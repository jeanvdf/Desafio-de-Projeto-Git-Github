print('Vamos Calcular os 10 Primeiros Termos de uma PA')
termo1 = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a razão: '))
c = 0
while c != 10:
    print('{} '.format(termo1), end='')
    termo1 += r
    c += 1
