print('Vamos Ler Dois Valores....')
resp = 'S'
r = 6
n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o Segundo Valor: '))
while resp == 'S' and r != 5:
    print('O Que Deseja Realizar Com os ValoreS? '
          '\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA')
    r = int(input('Digite a Opção: '))
    if r == 1:
        print('A Soma Entre os valores é {}.'.format(n1 + n2))
    elif r == 2:
        print('Os Dois Valores multiplicados é {}.'.format(n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('O Maior valor é {}.'.format(n1))
        if n2 > n1:
            print('O Maior Valor é {}.'.format(n2))
        if n1 == n2:
            print('Os Dois Valores são Iguais.')
    elif r == 4:
        print('Digite os Valores novamente..')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor:'))
    elif r != 5:
        print('Finalizando o Programa...')
    print('*'*30)
    resp = str(input('Deseja Continuar ? [S / N]')).upper().strip()
print('*'*32)
print('Fim do Programa. Volte Sempre !')
