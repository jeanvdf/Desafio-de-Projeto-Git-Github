print('-'*35)
print('Vamos Calcular os Termos de uma PA')
print('-'*35)
termo1 = int(input('Digite o 1º Termo: '))
r = int(input('Digite a Razão: '))
c = 0
resp = 10
total = 0
while resp != 0:
    total += resp
    while c != resp:
        print('{} '.format(termo1), end='')
        termo1 += r
        c += 1
    c = 0
    resp = int(input('\nVocê Deseja Calcular Mais Quantos Termos ? "\n[0] Para Encerrar"'))
print('Progressão Finalizada com {} Termos.'.format(total))
